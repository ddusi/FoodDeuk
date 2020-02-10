/**
 * jTinder initialization
 */
function Init() {
	$j311("#tinderslide").jTinder({
		// dislike callback
		onDislike: function (item) {
			// set the status text
			$j311('#status').html('Dislike image ' + (item.index() + 1));
			var id =$j311(item).attr('pk');
			console.log(id)
			$j311
			.ajax({
				url: '/swipe/likeornot/',
				type: 'GET',
				data: {
					'r_id' : id,
					'like_dislike' : 0
				},
				success: function (res) {
				}//success

			});//ajax


		},
		// like callback
		onLike: function (item) {
			// set the status text
			$j311('#status').html('Like image ' + (item.index() + 1));
			var id = $j311(item).attr('pk');
			console.log(id)
			$j311
			.ajax({
				url: '/swipe/likeornot/',
				type: 'GET',
				data: {
					'r_id' : id,
					'like_dislike' : 1
				},
				success: function (res) {
				}//success

			});//ajax

		},
		animationRevertSpeed: 200,
		animationSpeed: 400,
		threshold: 1,
		likeSelector: '.like',
		dislikeSelector: '.dislike'
	});

	/**
	 * Set button action to trigger jTinder like & dislike.
	 */
	$j311('.actions .like, .actions .dislike').click(function (e) {
		e.preventDefault();
		$j311("#tinderslide").jTinder($j311(this).attr('class'));
	});
}