var express = require('express');
var router = express.Router();
var http = require('https');
var request = require('request');

router.get('/', function(req, res) {
	var options = {
		host: 'openapi.youku.com',
		path: '/v2/oauth2/authorize?client_id=e342c22c049a5404&response_type=code&state=xyz&redirect_uri=http://www.ccpt.cc:3000/auths/redirect'
	};

	var callback = function(response) {
		var str = '';
		response.on('data', function (chunk) {
			str += chunk;
		});

		response.on('end', function() {
//			console.log(str);
			res.send(str);
		});
		console.log('start auth...');
	};

	http.request(options, callback).end();

  	//res.send('auth...');
});


router.get('/redirect', function(req, res) {
	var req_code = req.param('code');

	request.post(
		'https://openapi.youku.com/v2/oauth2/token',
		{form:{
					client_id:'e342c22c049a5404',
					client_secret:'faa1831867ddf26c496cd6365ca44ea2',
					grant_type:'authorization_code',
					code:req_code,
					redirect_uri:'http://www.ccpt.cc:3000/auths/redirect'
		
		}},

		function (error, response, body) {
			console.log(body);
			
			if (!error && response.statusCode == 200) {
				console.log(body);
			}
		}
		);

	console.log('auth redirect is active...');
});

router.get('/authcomplete', function(req, res) {
	
	console.log('authcomplete...');

	console.log(req);

	res.send('authcomplete...');
});

module.exports = router;
