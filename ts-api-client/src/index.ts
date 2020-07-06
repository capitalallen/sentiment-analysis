import { Hello } from './test-endpoint'
import { StockNewsPredict } from './stock-news-predict'

import { applyMixins } from './utils'
import { Base } from './base'

class Client extends Base {}
interface Client extends Hello {}
applyMixins(Client, [Hello,StockNewsPredict]);

export default Client
