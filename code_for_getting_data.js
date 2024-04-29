var canvas = document.querySelector('canvas');

var tooltip = document.querySelector('.chartjs-tooltip');

function simulateMouseMove(element, toX, y, callback) {
    var tooltipData = [];
    
    var fromX = element.getBoundingClientRect().left;
    var step = toX - fromX > 0 ? 1 : -1;
    var currentX = fromX;

    function move() {
        if ((step > 0 && currentX > toX) || (step < 0 && currentX < toX)) {
            callback(tooltipData);
            return;
        }

        var event = new MouseEvent('mousemove', {
            'view': window,
            'bubbles': true,
            'cancelable': true,
            'clientX': currentX,
            'clientY': y
        });
        element.dispatchEvent(event);
        
        setTimeout(function() {
            if (tooltip) {
                var tooltipDate = tooltip.querySelector('thead th').innerText;
                var tooltipValues = tooltip.querySelector('tbody').innerText;
                tooltipData.push({ date: tooltipDate, values: tooltipValues }); // 將日期和值添加到陣列中
            }
            
            currentX += step;
            move();
        }, 50);
    }

    move();
}

function arrayToCSV(data) {
    var csvContent = "data:text/csv;charset=utf-8,";
    csvContent += "Date,Sales,Rank,Price\r\n";
    data.forEach(function(item) {
        var row = [item.date].concat(Array.from(item.values.split('\n')).map(value => value.split(':')[1]?.replace(/,/g, '').trim())).join(",");
        csvContent += row + "\r\n";
    });
    return csvContent;
}

function downloadSalesCSV(data) {
    var csvContent = arrayToCSV(data);
    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "sales_data.csv");
    document.body.appendChild(link);
    link.click();
}

var tooltipRect = tooltip.getBoundingClientRect();
var y = tooltipRect.top + (tooltipRect.height / 2);

simulateMouseMove(canvas, canvas.getBoundingClientRect().right, y, function(data) {
    setTimeout(function() {
        downloadSalesCSV(data);
    }, 2000);
});
