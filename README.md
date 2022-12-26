# Java SQL:2016 Language Frontend
![Visit our Website.](https://manticore-projects.github.io/sql/index.html)

![Build Status](https://github.com/manticore-projects/sql/actions/workflows/maven.yml/badge.svg)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.facebook.presto/presto-coresql/badge.svg)](http://maven-badges.herokuapp.com/maven-central/com.facebook.presto/presto-coresql)
[![Javadocs](https://www.javadoc.io/badge/com.facebook.presto/presto-coresql.svg)](https://www.javadoc.io/doc/com.facebook.presto/presto-coresql)

A Modern SQL frontend based on SQL16 with extensions for streaming, graph, rich types, etc, including parser, resolver, rewriters, etc.

    * Comprehensive support for statements:

        - QUERY: ``SELECT ...``
        - DML: ``INSERT ... INTO ...`` ``UPDATE ...`` ``MERGE ... INTO ...`` ``DELETE ... FROM ...``
        - DDL: ``CREATE ...`` ``ALTER ...`` ``DROP ...``

    * Nested Expressions (e.g. Sub-Selects)
    * ``WITH`` clauses
    * De-Parser for a Statement AST Node, which writes a SQL from Java Objects

# How to use it

Maven Repository
```xml
<dependency>
        <groupId>com.facebook.presto</groupId>
        <artifactId>presto-coresql</artifactId>
        <version>0.1</version>
</dependency>
```

Parsing and Unparsing a SQL Statement
```
import com.facebook.coresql.parser.AstNode;
import com.facebook.coresql.parser.ParserHelper;
import com.facebook.coresql.parser.Unparser;

String sqlStr = "select 1 from dual where a=b";
AstNode ast = ParserHelper.parseStatement(sqlStr);
String unparsedSqlStr = Unparser.unparse(ast);
```

Compile latest version from source

```shell
git clone https://github.com/kaikalur/sql.git
cd sql
mvn install
```