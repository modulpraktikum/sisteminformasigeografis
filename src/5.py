import shapefile
w=shapefile.Writer()
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.save("soal5"