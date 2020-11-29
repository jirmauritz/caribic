// Namepspace
var th = {}

// init sockerIO
var socket = io();

th.xCenter = 50;
th.yCenter = 100;
th.stage = new createjs.Stage('throttle');

th.psp = new createjs.Shape();
th.psp.graphics.beginFill('#333333').drawRect(th.xCenter-35, th.yCenter - 5, 70, 10);

th.psp.alpha = 0.5;

th.vertical = new createjs.Shape();
th.vertical.graphics.beginFill('#ff4d4d').drawRect(50, 0, 2, 200);

th.horizontal = new createjs.Shape();
th.horizontal.graphics.beginFill('#ff4d4d').drawRect(th.xCenter-50, th.yCenter, 200, 2);

th.stage.addChild(th.psp);
th.stage.addChild(th.vertical);
th.stage.addChild(th.horizontal);
createjs.Ticker.framerate = 60;
createjs.Ticker.addEventListener('tick', th.stage);
th.stage.update();

var throttle = $('#throttle')[0];

th.hm = new Hammer.Manager(throttle, {
	recognizers: [
		[Hammer.Pan,{ direction: Hammer.DIRECTION_VERTICAL }],
		[Hammer.Tap]
	]
});

var update_throttle = function(ev) {
        var bb = ev.target.getBoundingClientRect();
        y = Math.min(Math.max(ev.center.y - bb.top - th.yCenter, -95), 95);
        if (th.psp.y != y) {
            value = Math.round( -100 * y / 95 );
            socket.emit('throttle', value);
            $('#tVal').text('Throttle: ' + value);
            th.psp.y = y;
            th.stage.update();
        }
    }

th.hm.on("panstart", function(ev) {
        th.psp.alpha = 1;
        th.stage.update();
    });

th.hm.on("pan", update_throttle);
th.hm.on("tap", update_throttle);

th.hm.on("panend", function(ev) {
        th.psp.alpha = 0.5;
        th.stage.update();
    });

var stopBtn = $('#stopBtn')[0];
stopBtn.onclick = function() {
    socket.emit('throttle', 0);
    $('#tVal').text('Throttle: 0');
    th.psp.y = 0;
    th.stage.update();
};
