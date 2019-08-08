/*jshint esversion: 6 */
function activate_graph() {
    let data = generate_data($('#num_cat').val());
    var activeTab = $('#tabs').tabs('option', 'active');
    if (activeTab === 0) {
        plotly_pie(data);
    } else if (activeTab === 1) {
        canvas_pie(data);
    } else if (activeTab === 2) {
        c3_pie(data);
    }
}

$(function () {
    $("#tabs").tabs({
        activate: function (event, ui) {
            activate_graph();
        }
    });

    activate_graph();
});

function generate_data(num) {
    let data = [];

    for (let i = 0; i < num; i++) {
        data.push(Math.floor(Math.random() * 100));
    }
    // for (let j = 0; j < lines; j++) {
    //     let line = [];
    //     for (let i = 0; i < num; i++) {
    //         line.push(Math.floor((Math.random() * 100)));
    //     }
    //     data.push(line);
    // }

    return data;
}

function plotly_pie(data) {

    let pie = [{
        values: data,
        type: 'pie'
    }];

    if ($('#plotly_labels').prop('checked')) {
        let labels = [];
        data.forEach(function (num, i) {
            labels[i] = `label${i}`;
        });
        pie.labels = labels;
    }

    let layout = {};

    // Title
    if ($('#plotly_title').prop('checked')) {
        layout.title = 'Plotly.js';
    }

    Plotly.newPlot('plotly_chart', pie, layout);

    $('#plotly_data').val(JSON.stringify(pie, undefined, 2));
    $('#plotly_layout').val(JSON.stringify(layout, undefined, 2));
}

function c3_pie(data) {
    let sections = [];
    data.forEach(function (num, i) {
        sections[i] = [
            `label${i}`,
            num
        ];
    });

    let chart_data = {
        data: {
            columns: sections,
            type: 'pie',
        },
        bindto: '#c3js_chart',
    };

    // Title
    if ($('#c3_title').prop('checked')) {
        chart_data.title = {
            text: 'C3js'
        };
    }

    c3.generate(chart_data);
}

function canvas_pie(data) {
    let sections = [];
    data.forEach(function (num, i) {
        sections.push({
            y: num,
            label: `label${i}`
        });
    });

    let chart_data = {
        data: [{
            type: "pie",
            dataPoints: sections
        }]
    };

    // Title
    if ($('#canvas_title').prop('checked')) {
        chart_data.title = {
            text: 'CanvasJS'
        };
    }

    var chart = new CanvasJS.Chart("canvas_chart", chart_data);

    chart.render();

}