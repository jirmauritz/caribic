// Namespace
var st = {}

st.xCenter = 150;
st.yCenter = 50;
st.stage = new createjs.Stage('steering');

st.psp = new createjs.Shape();
st.psp.graphics.beginFill('#333333').drawRect(st.xCenter-5, st.yCenter-35, 10, 70);

st.psp.alpha = 0.5;

st.vertical = new createjs.Shape();
st.horizontal = new createjs.Shape();
st.horizontal.graphics.beginFill('#ff4d4d').drawRect(0, 50, 300, 2);

st.stage.addChild(st.psp);
st.stage.addChild(st.vertical);
st.stage.addChild(st.horizontal);
createjs.Ticker.framerate = 60;
createjs.Ticker.addEventListener('tick', st.stage);
st.stage.update();

var steering = $('#steering')[0];

// create a simple instance
// by default, it only adds horizontal recognizers
st.hm = new Hammer(steering);

st.hm.on("press", function(ev) {
        st.psp.alpha = 1;

        var bb = ev.target.getBoundingClientRect();
        x = Math.max(Math.min(ev.center.x - bb.left - st.xCenter, 145), -145);
        st.psp.x = x;
        value = Math.round(100 * x / 145)
        $('#sVal').text('Steering: ' + value);

        st.stage.update();
    });

st.hm.on("pressup", function(ev) {
        st.psp.alpha = 0.5;
        createjs.Tween.get(st.psp).to({x: 0,y: 0}, 750, createjs.Ease.elasticOut);
        $('#sVal').text('Steering: ' + 0);
    });

st.hm.on("panstart", function(ev) {
        st.psp.alpha = 1;

        var bb = ev.target.getBoundingClientRect();
        x = Math.max(Math.min(ev.center.x - bb.left - st.xCenter, 145), -145);
        st.psp.x = x;
        value = Math.round(100 * x / 145)
        $('#sVal').text('Steering: ' + value);

        st.stage.update();
    });

// listen to events...
st.hm.on("panmove", function(ev) {
        var bb = ev.target.getBoundingClientRect();
        x = Math.max(Math.min(ev.center.x - bb.left - st.xCenter, 145), -145);
        st.psp.x = x;
        value = Math.round(100 * x / 145)
        $('#sVal').text('Steering: ' + value);

        st.stage.update();
    });

st.hm.on("panend", function(ev) {
        st.psp.alpha = 0.5;
        createjs.Tween.get(st.psp).to({x: 0,y: 0}, 750, createjs.Ease.elasticOut);
        $('#sVal').text('Steering: ' + 0);
    });