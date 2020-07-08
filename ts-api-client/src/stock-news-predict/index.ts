import qs from 'querystringify'
import { getPredict,predResult, postPredict } from './types'
import { Base } from '../base'

const resourceName = '/api/v1/stock-news-sentiment'

/**
 * hello 
 * extends base 
 * method
 *  - getPredict
 *  - postPredict 
 */
// /api/v1/stock-news-sentiment
export class StockNewsPredict extends Base {
    getNewsStockSentiment(params?: postPredict) {
        return this.request<predResult>(resourceName, {
            method: 'POST',
            body: JSON.stringify({ news: params })
        })
    }
}
