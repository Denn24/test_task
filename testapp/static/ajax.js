//js file
google.load('visualization', '1.0', {'packages':['corechart']});
function onAjax(value){
	$.ajax({
		url: "http://localhost:8000/index/ajax",
		type: "get",
		data:{input: document.getElementById("text-input").value, key: document.getElementById("text-key").value, choise: value},
		cache: false,
		success: function(data){
			console.log(data.map);
			map = data.map;
			$("#text-output").val(data.response);
			drawChart(map);
		}
	})
}

//Diagram of frequency
//This function was taken from htmlbook.ru/blog/grafiki-i-diagrammy
function drawChart(map) {
	tableList = [];
	metaDataList = [];
	metaDataList.push("char");
	metaDataList.push("count");
	tableList.push(metaDataList);
	for(item in map){
		localList = [];
		localList.push(item);
		localList.push(map[item]);
		tableList.push(localList);
	}
    var data = google.visualization.arrayToDataTable(tableList);
    var options = {
     title: 'Frequency of letters',
     hAxis: {title: 'letters'},
     vAxis: {title: 'frequency'}
    };
    var chart = new google.visualization.ColumnChart(document.getElementById('diagram'));
    chart.draw(data, options);
   }







