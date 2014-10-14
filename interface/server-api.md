Server API:
	1.  fetch my favorite videos:

		http://www.ccpt.cc:3000/apis/my_favorite_videos

		@ return a json structure, as following:
			{
			"count" : 20,
			"videos" :
			[
				{
					"id" : video_id,
					"title" : video_title,
					"link" : video_play_link,
					"thumbnail" : video_thumbnail,
					"duration" : video_duratin
				}
				...
			]
			}

		@ ps : the video_play_link is not m3u8 now! 
