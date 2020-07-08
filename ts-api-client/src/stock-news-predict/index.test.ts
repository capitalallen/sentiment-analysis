const nock = require('nock')
const Client = require('../../dist')

describe('Stock News Sentiment', () => {
    test('gt sentiment of a news', async () => {
        // Set up the mock request
        const scope = nock('http://127.0.0.1:5000/')
          .post('/api/v1/stock-news-sentiment')
          .reply(200, [{ pred: 'postive' }])

        // Make the request
        const client = new Client()
        await client.getNewsStockSentiment()

        // Assert that the expected request was made.
        scope.done()
    })
})

