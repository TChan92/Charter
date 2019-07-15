function activate_graph() {
    let data = generate_data($('#num_points').val(), $('#num_lines').val());
    var activeTab = $('#tabs').tabs('option', 'active');
    if (activeTab === 0) {
        plotly_line(data);
    } else if (activeTab === 1) {
        canvas_line(data);
    } else if (activeTab === 2) {
        c3_line(data);
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

function generate_data(num, lines) {
    let data = [];
    for (let j = 0; j < lines; j++) {
        let line = [];
        for (let i = 0; i < num; i++) {
            line.push(Math.floor((Math.random() * 100)));
        }
        data.push(line);
    }

    return data;
}

function plotly_line(data) {
    let traces = [];

    data.forEach(function (line) {
        let x = [...Array(line.length).keys()];

        var trace = {
            x: x,
            y: line,
            type: 'scatter'
        };

        traces.push(trace);

    });

    let layout = {};

    // Title
    if ($('#plotly_title').prop('checked')) {
        layout.title = 'Plotly.js';
    }

    // Enabled
    let scroll = $('input:radio[name=plotly_zoom]:checked').val();

    // Zoom options
    if (scroll === 'y') {
        layout.xaxis = {
            fixedrange: true
        };
    } else if (scroll === 'x') {
        layout.yaxis = {
            fixedrange: true
        };
    } else if (scroll === 'y') {
        layout.xaxis = {
            fixedrange: true
        };
    } else if (scroll === 'disabled') {
        layout.yaxis = {
            fixedrange: true
        };
        layout.xaxis = {
            fixedrange: true
        };
    }

    // If I wanted neater code I would initialize xaxis as blank so I wouldn't have to check for it.
    // But I want to the displayed code to be as minimal as possible
    if ($("#plotly_xaxis").prop('checked')) {
        if (layout.hasOwnProperty('xaxis')) {
            layout.xaxis.title = {
                text:'xaxis'
            }
        } else {
            layout.xaxis = {
                title: {
                    text: 'xaxis'
                }
            };
        }
    }
    
    if ($("#plotly_yaxis").prop('checked')) {
        if (layout.hasOwnProperty('yaxis')) {
            layout.yaxis.title = {
                text:'yaxis'
            };
        } else {
            layout.yaxis = {
                title: {
                    text: 'yaxis'
                }
            };
        }
    }
    $('#plotly_data').val(JSON.stringify(traces, undefined, 2));
    $('#plotly_layout').val(JSON.stringify(layout, undefined, 2));

    Plotly.newPlot('plotly_chart', traces, layout);

}

function c3_line(data) {
    let lines = [];

    data.forEach(function (line, index) {
        lines.push([`line${index}`].concat(line))
    });

    let chart_data = {
        bindto: '#c3js_chart',
        data: {
            columns: lines
        }
    };

    let scroll = $('input:radio[name=c3_zoom]:checked').val();

    // Scroll zoom
    if (scroll === 'scroll') {
        chart_data.zoom = {
            enabled: true,
            type: 'scroll'
        };
    //    Drag zoom
    } else if (scroll === 'drag') {
        chart_data.zoom = {
            enabled: true,
            type: 'drag'
        };
    }

    // Title
    if ($('#c3_title').prop('checked')) {
        chart_data.title = {
            text: 'C3js'
        };
    }

    // Xaxis
    if ($('#c3_xaxis').prop('checked')) {
        chart_data.axis = {
            x: {
                label: 'xaxis',
            }
        };
    }

    // Yaxis
    if ($('#c3_yaxis').prop('checked')) {
        if (chart_data.hasOwnProperty('axis')) {
            chart_data.axis.y = {
                label: 'yaxis'
            };
        } else {
            chart_data.axis = {
                y: {
                    label: 'yaxis',
                }
            };
        }
    }

    c3.generate(chart_data);

    $('#c3_source').val(JSON.stringify(chart_data, undefined, 2));
}

function canvas_line(data) {
    let lines = [];

    data.forEach(function (line) {
        let l = {
            type: "line",
            dataPoints: line.map(function (y) {
                return {y: y}
            })
        };
        lines.push(l);
    });

    var chart = new CanvasJS.Chart("canvas_chart", {
        title: {
            text: "CanvasJS"
        },
        data: lines
    });
    chart.render();
}