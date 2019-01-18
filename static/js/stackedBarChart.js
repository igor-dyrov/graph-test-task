const xData = ['first', 'second', 'third'];

const margin = {top: 20, right: 50, bottom: 30, left: 50},
	width = 400 - margin.left - margin.right,
	height = 300 - margin.top - margin.bottom;

const x = d3.scale.ordinal()
	.rangeRoundBands([0, width], .35);

const y = d3.scale.linear()
	.rangeRound([height, 0]);

const color = d3.scale.category20();

const xAxis = d3.svg.axis()
	.scale(x)
	.orient('bottom');

const svg = d3.select('body').append('svg')
	.attr('width', width + margin.left + margin.right)
	.attr('height', height + margin.top + margin.bottom)
	.append('g')
	.attr('transform', 'translate(' + margin.left + '', '' + margin.top + ')');

d3.json('/api/get_sample_data', (error, data) => {
	if (!error) {
		const dataIntermediate = xData.map((c) => data.map((d) => {
		return {x: d.employee, y: d[c]};
	}));

	console.log(dataIntermediate);

	const dataStackLayout = d3.layout.stack()(dataIntermediate);

	x.domain(dataStackLayout[0].map((d) => d.x));

	y.domain([0,
		d3.max(dataStackLayout[dataStackLayout.length - 1],
			(d) => d.y0 + d.y)
	])
		.nice();

	const layer = svg.selectAll('.stack')
		.data(dataStackLayout)
		.enter().append('g')
		.attr('class', 'stack')
		.style('fill', (d, i) => color(i));

	layer.selectAll('rect')
		.data((d) => d)
		.enter().append('rect')
		.attr('x', (d) => x(d.x))
		.attr('y', (d) => y(d.y + d.y0))
		.attr('height', (d) => y(d.y0) - y(d.y + d.y0))
		.attr('width', x.rangeBand());

	svg.append('g')
		.attr('class', 'axis')
		.attr('transform', 'translate(0,' + height + ')')
		.call(xAxis);
	}
});