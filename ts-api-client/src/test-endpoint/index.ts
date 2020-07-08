import qs from 'querystringify'
import { HelloGet, HelloPost, predResult } from './types'
import { Base } from '../base'

const resourceName = 'test'

/**
 * hello 
 * extends base 
 * method
 *  - getHello
 *  - postHello 
 */
// api/v1/test-endpoint/?
export class Hello extends Base {
    getHello(params?: HelloGet){
        let query = `${resourceName}`;
        if (params){
            query+= qs.stringify(params,"?")
        }
        return this.request<predResult>(query)
    }

    postHello(params?: HelloPost) {
        return this.request<HelloPost>(resourceName, {
            method: 'POST',
            body: JSON.stringify({ text: params })
        })
    }
}
