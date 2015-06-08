;
/*! test-markdown 05-06-2015 */
(function () {
    /**
     * Created by miles on 6/5/15.
     */

    var converter = new showdown.Converter({extensions: ['table']});

    function Editor(input, preview) {
        this.update = function () {
            preview.innerHTML = converter.makeHtml(input.value);
        };
        input.editor = this;
        this.update();
    }

    var $ = function (id) {
        return document.getElementById(id);
    };
    new Editor($("markdown"), $("preview"));

}).call(this);