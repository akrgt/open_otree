/* Contains variables and actions specific to the discrete version of the slider measure */

var num_discrete_steps = 8;

/* Create each slider and attach the necessary event handlers */

var item1_slider = $('#item1').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item1', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item1_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item1', proportional_position_on_slider);
}).data('slider');

var item2_slider = $('#item2').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item2', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item2_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item2', proportional_position_on_slider);
}).data('slider');

var item3_slider = $('#item3').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item3', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item3_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item3', proportional_position_on_slider);
}).data('slider');

var item4_slider = $('#item4').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item4', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item4_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item4', proportional_position_on_slider);
}).data('slider');

var item5_slider = $('#item5').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item5', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item5_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item5', proportional_position_on_slider);
}).data('slider');

var item6_slider = $('#item6').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item6', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item6_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item6', proportional_position_on_slider);
}).data('slider');

var item7_slider = $('#item7').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item7', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item7_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item7', proportional_position_on_slider);
}).data('slider');


var item8_slider = $('#item8').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item8', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item8_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item8', proportional_position_on_slider);
}).data('slider');


var item9_slider = $('#item9').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item9', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item9_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item9', proportional_position_on_slider);
}).data('slider');

var item10_slider = $('#item10').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item10', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item10_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item10', proportional_position_on_slider);
}).data('slider');


var item11_slider = $('#item11').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item11', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item11_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item11', proportional_position_on_slider);
}).data('slider');

var item12_slider = $('#item12').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item12', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item12_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item12', proportional_position_on_slider);
}).data('slider');


var item13_slider = $('#item13').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item13', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item13_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item13', proportional_position_on_slider);
}).data('slider');

var item14_slider = $('#item14').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item14', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item14_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item14', proportional_position_on_slider);
}).data('slider');

var item15_slider = $('#item15').slider({
    formatter: function(value) {
        var proportional_position_on_slider = (value - 1) / num_discrete_steps;
        return tooltip_text('item15', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item15_slider.getValue();
    var proportional_position_on_slider = (value-1) / 8;
    update_displayed_values('item15', proportional_position_on_slider);
}).data('slider');








/* Update all displayed values for the first time */

update_displayed_values('item1', (item1_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item2', (item2_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item3', (item3_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item4', (item4_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item5', (item5_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item6', (item6_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item7', (item1_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item8', (item2_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item9', (item3_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item10', (item4_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item11', (item5_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item12', (item6_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item13', (item4_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item14', (item5_slider.getValue() - 1) / num_discrete_steps);
update_displayed_values('item15', (item6_slider.getValue() - 1) / num_discrete_steps);