import { EclairRest, IBackend, LndRest } from './backends'
import { EBackendType } from './enums'
import { IEclairRest, ILndRest, Invoice } from './interfaces'

export class Una {
  private readonly client: IBackend | undefined

  constructor (backend: EBackendType, connectionInformation: ConnectionInformation) {
    if (!this.verifyConnectionInformation(connectionInformation, backend)) {
      throw new Error('connectionInformation is not correct for the type ' + backend)
    }

    if (backend === EBackendType.LndRest) {
      const info = connectionInformation as ILndRest
      this.client = new LndRest({ url: info.url, hexMacaroon: info.hexMacaroon })
    } else if (backend === EBackendType.EclairRest) {
      const info = connectionInformation as IEclairRest
      this.client = new EclairRest({ url: info.url, user: info.user, password: info.password })
    } else {
      throw new Error('Backend not supported.')
    }
  }

  /**
       * Create an invoice
       * @param amount amount in satoshis
       * @param memo memo
       * @returns Invoice
       */
  public async createInvoice (amount: number, memo: string): Promise<Invoice> {
    if (this.client === undefined) {
      throw new Error('No backend defined')
    }

    return await this.client.createInvoice(amount, memo)
  }

  /**
       * Get an invoice previously created
       * @param hash hex encoded payment hash
       * @returns Invoice
       */
  public async getInvoice (hash: string): Promise<Invoice> {
    if (this.client === undefined) {
      throw new Error('No backend defined')
    }

    return await this.client.getInvoice(hash)
  }

  private verifyConnectionInformation (connectionInformation: ConnectionInformation, backend: EBackendType): boolean {
    if (backend === EBackendType.LndRest) {
      const info = connectionInformation as ILndRest
      return info.url !== undefined && info.hexMacaroon !== undefined
    }
    if (backend === EBackendType.EclairRest) {
      const info = connectionInformation as IEclairRest
      return info.url !== undefined && info.user !== undefined && info.password !== undefined
    }
    return false
  }
}

type ConnectionInformation = ILndRest | IEclairRest
