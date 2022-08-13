use crate::backends::lnd::rest::node::LndRest;
use crate::error::Error;
use crate::types::{Backend, CreateInvoiceParams, NodeConfig, NodeInfo};

#[async_trait::async_trait]
pub trait NodeMethods {
    async fn create_invoice(&self, invoice: CreateInvoiceParams) -> Result<String, Error>;
    async fn get_info(&self) -> Result<NodeInfo, Error>;
}

pub struct Node {
    pub backend: Backend,
    pub node: Box<dyn NodeMethods + Send + Sync>,
}

impl Node {
    pub fn new(backend: Backend, config: NodeConfig) -> Result<Self, Error> {
        match backend {
            Backend::LndRest => {
                let node = LndRest::new(config).unwrap();
                Ok(Node {
                    backend,
                    node: Box::new(node),
                })
            }
            _ => Err(Error::InvalidBackend),
        }
    }
}

#[async_trait::async_trait]
impl NodeMethods for Node {
    async fn create_invoice(&self, invoice: CreateInvoiceParams) -> Result<String, Error> {
        self.node.create_invoice(invoice).await
    }

    async fn get_info(&self) -> Result<NodeInfo, Error> {
        self.node.get_info().await
    }
}
