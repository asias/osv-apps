from osv.modules import api

api.require('java')

# RAMDirectory MMapDirectory
# /data/lucene/indices/wikimedium10k.trunk.Lucene41.Memory.nd0.01M/facets
default = api.run("/hello.so & /java.so  -Djava.rmi.server.hostname=192.168.66.12 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Xms2g -Xmx2g -classpath /data/lucene/trunk/lucene/build/core/classes/java:/data/lucene/trunk/lucene/build/core/classes/test:/data/lucene/trunk/lucene/build/sandbox/classes/java:/data/lucene/trunk/lucene/build/misc/classes/java:/data/lucene/trunk/lucene/build/facet/classes/java:/data/lucene/trunk/lucene/build/analysis/common/classes/java:/data/lucene/trunk/lucene/build/analysis/icu/classes/java:/data/lucene/trunk/lucene/build/queryparser/classes/java:/data/lucene/trunk/lucene/build/grouping/classes/java:/data/lucene/trunk/lucene/build/suggest/classes/java:/data/lucene/trunk/lucene/build/highlighter/classes/java:/data/lucene/trunk/lucene/build/codecs/classes/java:/data/lucene/trunk/lucene/build/queries/classes/java:/data/lucene/util/lib/HdrHistogram.jar:/data/lucene/util/build perf.SearchPerfTest -dirImpl RAMDirectory  -indexPath /data/lucene/indices/wikimedium10k.trunk.Lucene41.Memory.nd0.01M -analyzer StandardAnalyzer -taskSource /data/lucene/util/my.tasks -searchThreadCount 1 -taskRepeatCount 200000 -field body -tasksPerCat 1 -staticSeed -3217382 -seed -1079703 -similarity DefaultSimilarity -commit multi -hiliteImpl FastVectorHighlighter -log /data/lucene/logs/test.A.0 -topN 10")
