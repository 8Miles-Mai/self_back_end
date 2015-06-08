;
/*! test-markdown 05-06-2015 */
(function () {
	/**
	 * Created by miles on 6/8/15.
	 */
	var converter = new showdown.Converter({extensions: ['table']});

	function Preview(preview) {
		this.format = function () {
			console.log(preview.innerText);
			console.log(preview.innerHTML);
			console.log(preview.value);
			preview.innerHTML = converter.makeHtml(preview.innerText);
//			preview.innerHTML = preview.innerText;
		};
		preview.preview = this;
		this.format();
	}

	var $ = function (id) {
		return document.getElementById(id);
	};
	new Preview($("preview"));
}).call(this);