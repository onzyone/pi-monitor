function computeSunrise(e,t){
	var n=13.408056;
	var r=52.518611;
	var i=90.83333333333333;
	var s=Math.PI/180;	
	var o=180/Math.PI;
	var u=n/15;
	var a;
	if(t){
		a=e+(6-u)/24
	}
	else{
		a=e+(18-u)/24
	}
	M=.9856*a-3.289;
	L=M+1.916*Math.sin(M*s)+.02*Math.sin(2*M*s)+282.634;
	if(L>360){
		L=L-360
	}
	else if(L<0){
		L=L+360
	}	
	RA=o*Math.atan(.91764*Math.tan(L*s));
	if(RA>360){
		RA=RA-360
	}else if(RA<0){
		RA=RA+360
	}
	Lquadrant=Math.floor(L/90)*90;
	RAquadrant=Math.floor(RA/90)*90;
	RA=RA+(Lquadrant-RAquadrant);
	RA=RA/15;
	sinDec=.39782*Math.sin(L*s);
	cosDec=Math.cos(Math.asin(sinDec));
	cosH=(Math.cos(i*s)-sinDec*Math.sin(r*s))/(cosDec*Math.cos(r*s));
	var f;
	if(t){
		f=360-o*Math.acos(cosH)
	}else{
		f=o*Math.acos(cosH)
	}
	f=f/15;
	T=f+RA-.06571*a-6.622;
	UT=T-u;
	if(UT>24){
		UT=UT-24
	}else if(UT<0){
		UT=UT+24
	}
	localT=UT+2;
	return localT*3600*1e3
}


function dayOfYear(){
	var e=Math.floor((new Date).setFullYear((new Date).getFullYear(),0,1)/864e5);
	var t=Math.ceil((new Date).getTime()/864e5);
	var n=t-e;
	return n
}
	Highcharts.setOptions({
		global:{useUTC:false}});
		options={chart:{renderTo:"content",type:"spline"},title:{text:"Temperatures of the last 24h"},subtitle:{text:""},xAxis:{type:"datetime",dateTimeLabelFormats:{hour:"%H. %M"}},yAxis:{title:{text:"T (°C)"}},tooltip:{formatter:function(){return"<b>"+this.series.name+"</b><br/>"+Highcharts.dateFormat("%H:%M",this.x)+": "+this.y.toFixed(1)+"°C"}},plotOptions:{series:{marker:{radius:2}}},lineWidth:1,series:[]}
