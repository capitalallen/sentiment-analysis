const Client = require('../dist/index');

const client = new Client()

/*DevToClient.getMyArticles().then((data) => {
    console.log(data)
})*/


client.postPredict("hello going down").then((data) => {
    console.log(data)
}).catch(err=>{
    console.log(err)
})

// DevToClient.getFollowers().then((data) => {
//     console.log(data)
// })
