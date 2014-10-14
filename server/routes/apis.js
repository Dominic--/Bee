var express = require('express');
var router = express.Router();
var http = require('https');
var request = require('request');

router.get('/my_favorite_videos', function(req, res) {
	var options = {
		host: 'openapi.youku.com',
		path: '/v2/videos/favorite/by_me.json?client_id=e342c22c049a5404&access_token=d5aaaa90763e835106e5d4e195c343db&orderby=favorite-time&page=1&count=20'
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
		console.log('get my videos...');
	};

	http.request(options, callback).end();

});

module.exports = router;
