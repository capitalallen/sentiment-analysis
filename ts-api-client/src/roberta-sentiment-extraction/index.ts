import qs from 'querystringify'
import {predResult, postPredict } from './types'
import { Base } from '../base'

const resourceName = '/api/v1/sentiment-extraction'

/**
 * hello 
 * extends base 
 * method
 *  - getPredict
 *  - postPredict 
 */
// /api/v1/stock-news-sentiment
export class SentimentExtraction extends Base {
    getSentimentExtraction(params?: postPredict) {
        return this.request<predResult>(resourceName, {
            method: 'POST',
            body: JSON.stringify({ news: params })
        })
    }
}
