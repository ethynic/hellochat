var bot = new ChatSDK({
    config: {
      navbar: {
        title: '开发助手'
      },
      robot: {
        avatar: 'https://gw.alicdn.com/tfs/TB1U7FBiAT2gK0jSZPcXXcKkpXa-108-108.jpg'
      },
      messages: [
        {
          type: 'text',
          content: {
            text: '我是您的开发小助手，请问有什么可以帮您？'
          }
        }
      ]
    },

    requests: {
      send: function (msg) {
        if (msg.type === 'text') {
          return {
            headers: {'Content-Type': 'application/json'},
            url: 'http://127.0.0.1:5000/anwser',
            body: JSON.stringify({
              question: msg.content.text
            }),
            method: 'POST'
          };
        }
      }
      },


      handlers: {
      parseResponse: function (res, requestType) {
        // 根据 requestType 处理数据
        if (requestType === 'send' && res) {
            var response = {
                type:'text',
                content:{
                    text:''
                }
            };
            if (!res.errmsg) 
              response.content.text = res.choices[0].message.content;
            else 
              response.content.text = res.message;
            console.log(response);
            res = response;
            return res;
        }
  
        // 不需要处理的数据直接返回
        return res;
      },
    }
  });
  
  bot.run();