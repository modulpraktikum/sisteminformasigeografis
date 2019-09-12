services:
demo:
tms:
	use_grid_names: true
	origin: 'nw'
   kml
	use_grid_names: true
   wmts:

	restful: true

	resful_template: '/{llayer}/{TileMatrixSet}/{{TileMatrix}/{TileCol}/{TileRow}.{Format}'
	
	kvp: true
	md:


		title: Awangga GeoMap
		abstract: This is the Awangga Geomap.
		online_resource http://www.awangga.net/
		contact:
			person: Rolly Maulana Awangga
			position: Software Engineer
			organiztion: Belant Persada
			address: Jl. Ligar Nyawang No.2