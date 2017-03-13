#!/bin/bash
unzip -q ./backups.zip -d ./
curl -XPUT http://localhost:9200/_snapshot/test-elastic-backup -d '{"type":"fs","settings":{"compress": true,"location":"test-elastic"}}'
curl -XPOST http://localhost:9200/_snapshot/test-elastic-backup/mars72017/_restore
