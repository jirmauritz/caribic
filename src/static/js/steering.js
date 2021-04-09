// Namespace
var st = {}

// init sockerIO
var socket = io();

st.xCenter = 150;
st.yCenter = 50;
st.stage = new createjs.Stage('steering');

st.psp = new createjs.Shape();
st.psp.graphics.beginFill('#333333').drawRect(st.xCenter-5, st.yCenter-35, 10, 70);

st.psp.alpha = 0.5;

st.horizontal = new createjs.Shape();
st.horizontal.graphics.beginFill('#ff4d4d').drawRect(0, 50, 300, 2);

st.stage.addChild(st.psp);
st.stage.addChild(st.horizontal);
createjs.Ticker.framerate = 60;
createjs.Ticker.addEventListener('tick', st.stage);
st.stage.update();

var steering = $('#steering')[0];

st.hm = new Hammer(steering);

var update_steering = function(ev) {
    var bb = ev.target.getBoundingClientRect();
    x = Math.max(Math.min(ev.center.x - bb.left - st.xCenter, 145), -145);
    if (st.psp.x != x) {
        value = Math.round(100 * x / 145)
        socket.emit('steering', value);
        $('#sVal').text('Steering: ' + value);
        st.psp.x = x;
        st.stage.update();
    }
}

var reset_steering = function(ev) {
        socket.emit('steering', 0);
        st.psp.alpha = 0.5;
        createjs.Tween.get(st.psp).to({x: 0,y: 0}, 750, createjs.Ease.elasticOut);
        $('#sVal').text('Steering: ' + 0);
    }

st.hm.on("press", update_steering);
st.hm.on("pressup", reset_steering);

st.hm.on("panstart", function(ev) {
        st.psp.alpha = 1;
        st.stage.update();
    });

st.hm.on("panmove", update_steering);

st.hm.on("panend", reset_steering);