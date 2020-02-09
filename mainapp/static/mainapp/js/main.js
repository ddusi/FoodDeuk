/**
 * jTinder initialization
 */
function Init() {
	$("#tinderslide").jTinder({
		// dislike callback
		onDislike: function (item) {
			// set the status text
			$('#status').html('Dislike image ' + (item.index() + 1));
			var id =$(item).attr('pk');
			console.log(id)
			$
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
			$('#status').html('Like image ' + (item.index() + 1));
			var id = $(item).attr('pk');
			console.log(id)
			$
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
	$('.actions .like, .actions .dislike').click(function (e) {
		e.preventDefault();
		$("#tinderslide").jTinder($(this).attr('class'));
	});
}