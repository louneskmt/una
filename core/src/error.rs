use std::{
    fmt::{self, Display},
    io::ErrorKind,
};

#[derive(Debug)]
pub enum ConfigError {
    MissingField(String),
    InvalidField(String),
    ParsingHexError(String),
}

impl Display for ConfigError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ConfigError::MissingField(field) => write!(f, "Missing field: {}", field),
            ConfigError::InvalidField(field) => write!(f, "Invalid field: {}", field),
            ConfigError::ParsingHexError(field) => {
                write!(f, "Error parsing field {}: expected hex string", field)
            }
        }
    }
}

#[derive(Debug)]
pub enum Error {
    MissingBackend,
    InvalidBackend,
    Unauthorized,
    NotImplemented,
    ConfigError(ConfigError),
    ConnectionError(String),
    ApiError(String),
    UnknownError(String),
    ConversionError(String),
}

impl Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let str = match self {
            Error::InvalidBackend => String::from("invalid backend"),
            Error::MissingBackend => String::from("missing backend"),
            Error::Unauthorized => String::from("unauthorized credentials"),
            Error::NotImplemented => String::from("not implemented"),
            Error::ConfigError(err) => err.to_string(),
            Error::ConnectionError(err) => err.to_string(),
            Error::ApiError(err) => err.clone(),
            Error::ConversionError(err) => err.clone(),
            Error::UnknownError(err) => err.clone(),
        };

        write!(f, "{}", str)
    }
}

impl From<reqwest::Error> for Error {
    fn from(err: reqwest::Error) -> Self {
        if err.is_timeout() {
            let message = match err.url() {
                Some(url) => format!("timeout: {}", url),
                None => String::from("timeout"),
            };
            Error::ConnectionError(message)
        } else if err.is_connect() {
            let message = match err.url() {
                Some(url) => format!("couldn't connect to {}", url),
                None => err.to_string(),
            };
            Error::ConnectionError(message)
        } else if err.is_builder() {
            Error::ConnectionError(err.to_string().replace("builder error: ", ""))
        } else {
            Error::ApiError(err.to_string())
        }
    }
}

impl From<tonic::transport::Error> for Error {
    fn from(err: tonic::transport::Error) -> Self {
        Error::ApiError(err.to_string())
    }
}

impl From<reqwest::header::InvalidHeaderValue> for Error {
    fn from(err: reqwest::header::InvalidHeaderValue) -> Self {
        Error::ApiError(err.to_string())
    }
}

impl From<tonic::Status> for Error {
    fn from(status: tonic::Status) -> Self {
        Error::ApiError(status.message().to_string())
    }
}

impl From<ConfigError> for Error {
    fn from(err: ConfigError) -> Self {
        Error::ConfigError(err)
    }
}

impl From<Error> for std::io::Error {
    fn from(e: Error) -> std::io::Error {
        std::io::Error::new(ErrorKind::Other, e.to_string())
    }
}
