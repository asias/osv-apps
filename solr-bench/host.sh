#taskRepeatCount=50000
taskRepeatCount=200000
topN=10
searchThreadCount=1
tasksPerCat=1

cd upstream

java -Djava.rmi.server.hostname=192.168.122.89 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Xms2g -Xmx2g -classpath ./trunk/lucene/build/core/classes/java:./trunk/lucene/build/core/classes/test:./trunk/lucene/build/sandbox/classes/java:./trunk/lucene/build/misc/classes/java:./trunk/lucene/build/facet/classes/java:/home/mike/src/lucene-c-boost/dist/luceneCBoost-SNAPSHOT.jar:./trunk/lucene/build/analysis/common/classes/java:./trunk/lucene/build/analysis/icu/classes/java:./trunk/lucene/build/queryparser/classes/java:./trunk/lucene/build/grouping/classes/java:./trunk/lucene/build/suggest/classes/java:./trunk/lucene/build/highlighter/classes/java:./trunk/lucene/build/codecs/classes/java:./trunk/lucene/build/queries/classes/java:./util/lib/HdrHistogram.jar:./util/build perf.SearchPerfTest -dirImpl RAMDirectory -indexPath ./indices/wikimedium10k.trunk.Lucene41.Memory.nd0.01M/ -analyzer StandardAnalyzer -taskSource ./util/my.tasks -searchThreadCount $searchThreadCount -taskRepeatCount $taskRepeatCount -field body -tasksPerCat $tasksPerCat -staticSeed -3217382 -seed -1079703 -similarity DefaultSimilarity -commit multi -hiliteImpl FastVectorHighlighter -log logs/test.B.0 -topN $topN

#cp logs/test.A.0 logs/test.B.0
#cp logs/test.A.0.stdout logs/test.B.0.stdout
#./result.sh
#python -m SimpleHTTPServer 8000
