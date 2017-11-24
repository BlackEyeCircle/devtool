import math

pi = 3.14159265358979324;
a = 6378245.0;
ee = 0.00669342162296594323;
x_pi = 3.14159265358979324 * 3000.0 / 180.0;

def wgs2bd(lat, lon):
	wgs2gcjres = wgs2gcj(lat, lon);
	gcj2bdres = gcj2bd(wgs2gcjres[0], wgs2gcjres[1]);
	return gcj2bdres;


def gcj2bd(lat, lon):
	x = lon
	y = lat;
	z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi);
	theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi);
	bd_lon = z * math.cos(theta) + 0.0065;
	bd_lat = z * math.sin(theta) + 0.006;
	return [bd_lat, bd_lon]


def bd2gcj( lat,  lon):
	x = lon - 0.0065
	y = lat - 0.006;
	z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi);
	theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi);
	gg_lon = z * math.cos(theta);
	gg_lat = z * math.sin(theta);
	return [gg_lat, gg_lon]


def wgs2gcj(lat, lon):
	dLat = transformLat(lon - 105.0, lat - 35.0);
	dLon = transformLon(lon - 105.0, lat - 35.0);
	radLat = lat / 180.0 * pi;
	magic = math.sin(radLat);
	magic = 1 - ee * magic * magic;
	sqrtMagic = math.sqrt(magic);
	dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * pi);
	dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * pi);
	mgLat = lat + dLat;
	mgLon = lon + dLon;
	loc = [mgLat, mgLon]
	return loc;


def transformLat(lat, lon):
	ret = -100.0 + 2.0 * lat + 3.0 * lon + 0.2 * lon * lon + 0.1 * lat * lon + 0.2 * math.sqrt(abs(lat));
	ret += (20.0 * math.sin(6.0 * lat * pi) + 20.0 * math.sin(2.0 * lat * pi)) * 2.0 / 3.0;
	ret += (20.0 * math.sin(lon * pi) + 40.0 * math.sin(lon / 3.0 * pi)) * 2.0 / 3.0;
	ret += (160.0 * math.sin(lon / 12.0 * pi) + 320 * math.sin(lon * pi/ 30.0)) * 2.0 / 3.0;
	return ret;


def transformLon(lat, lon):
	ret = 300.0 + lat + 2.0 * lon + 0.1 * lat * lat + 0.1 * lat * lon + 0.1 * math.sqrt(abs(lat));
	ret += (20.0 * math.sin(6.0 * lat * pi) + 20.0 * math.sin(2.0 * lat * pi)) * 2.0 / 3.0;
	ret += (20.0 * math.sin(lat * pi) + 40.0 * math.sin(lat / 3.0 * pi)) * 2.0 / 3.0;
	ret += (150.0 * math.sin(lat / 12.0 * pi) + 300.0 * math.sin(lat / 30.0 * pi)) * 2.0 / 3.0;
	return ret;




import os;

document = open("abc.kml", "r",encoding='UTF-8');
outile = open("gps.txt","w");


content = document.readline();

doors = content.split()
for door in doors:
	val = door.split(',');
	print(val)
	newval = wgs2bd(float(val[1].encode('utf-8').decode('utf-8-sig')), float(val[0].encode('utf-8').decode('utf-8-sig')))
	outstr = "new BMap.Point(%f,%f),"%(newval[1], newval[0])
	outile.write(outstr)
outile.close()


# var points = [ 
#   new BMap.Point(117.270591,23.812975), 
#   new BMap.Point(117.227819,23.814327), 
#   new BMap.Point(117.171452,23.800036), 
#   new BMap.Point(117.132368,23.791609), 
#   new BMap.Point(117.076919,23.764658), 
#   new BMap.Point(117.024827,23.754510), 
#   new BMap.Point(116.981047,23.739533), 
#   new BMap.Point(116.939091,23.717617), 
#   new BMap.Point(116.900199,23.699399), 
#   new BMap.Point(116.885031,23.689196), 
#   new BMap.Point(116.874584,23.679668), 
#   new BMap.Point(116.811841,23.626940), 
#   new BMap.Point(116.759632,23.604713), 
#   new BMap.Point(116.725061,23.587160), 
#   new BMap.Point(116.651402,23.566650), 
#   new BMap.Point(116.595323,23.545934), 
#   new BMap.Point(116.565463,23.533553), 
#   new BMap.Point(116.552337,23.519046), 
#   new BMap.Point(116.544596,23.508704), 
#   new BMap.Point(116.537630,23.464337), 
#   new BMap.Point(116.528264,23.443634), 
#   new BMap.Point(116.518571,23.425543), 
#   new BMap.Point(116.502256,23.414608), 
#   new BMap.Point(116.429954,23.388459), 
#   new BMap.Point(116.388039,23.368854), 
#   new BMap.Point(116.352537,23.347284), 
#   new BMap.Point(116.281605,23.327247), 
#   new BMap.Point(116.227800,23.293717), 
#   new BMap.Point(116.214108,23.280499), 
#   new BMap.Point(116.180527,23.247139), 
#   new BMap.Point(116.107918,23.134458), 
#   new BMap.Point(116.040802,23.102683), 
#   new BMap.Point(116.005375,23.071510), 
#   new BMap.Point(115.979189,23.052335), 
#   new BMap.Point(115.874687,23.017842), 
#   new BMap.Point(115.732058,22.949055), 
#   new BMap.Point(115.650940,22.903134), 
#   new BMap.Point(115.559445,22.859811), 
# ];//设置坐标数组


context = document.read();
document.close();

