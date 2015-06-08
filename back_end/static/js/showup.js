;
/*! test-markdown 05-06-2015 */
(function () {
	/**
	 * Created by miles on 6/8/15.
	 */
	var converter = new showdown.Converter({extensions: ['table']});

	function Preview(input, preview) {
		this.format = function () {
			console.log(input.innerText);
			console.log(input.innerHTML);
			console.log(input.value);
			preview.innerHTML = converter.makeHtml(input.value);
//			preview.innerHTML = preview.innerText;
		};
		input.preview = this;
		this.format();
	}

	var $ = function (id) {
		return document.getElementById(id);
	};
	new Preview($("input"), $("preview"));
}).call(this);