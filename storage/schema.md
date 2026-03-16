# {serviceName} 数据库结构文档

**创建日期**: {date:-2026-03-16}
**数据库管理员**: {dba}
**版本**: {version:-1.0}

## 概述

本文档描述 {serviceName} 微服务的数据库结构设计。

## 数据库信息

### 数据库类型

{databaseType}

### 数据库版本

{databaseVersion}

### 数据库名称

{databaseName}

## 表结构

### {table1}

#### 表信息

- **表名**: {table1}
- **描述**: {tableDescription1}
- **存储引擎**: {storageEngine1}

#### 字段定义

| 字段名     | 类型        | 长度       | 允许NULL     | 默认值         | 描述        | 索引      |
| ---------- | ----------- | ---------- | ------------ | -------------- | ----------- | --------- |
| {field1}   | {type1}     | {length1}   | {nullable1}   | {defaultValue1} | {description1} | {index1}  |
| {field2}   | {type2}     | {length2}   | {nullable2}   | {defaultValue2} | {description2} | {index2}  |

#### 主键

{primaryKey1}

#### 外键

| 外键名         | 引用表          | 引用字段        | 描述        |
| -------------- | --------------- | --------------- | ----------- |
| {foreignKey1}  | {referencedTable1} | {referencedField1} | {description1} |

#### 索引

| 索引名     | 索引类型     | 索引字段       | 描述        |
| ---------- | ------------ | -------------- | ----------- |
| {index1}   | {indexType1} | {indexFields1} | {description1} |

## 实体关系图

```mermaid
erDiagram
    {TABLE1} {
        {field1} {type1}
        {field2} {type2}
    }
    {TABLE2} {
        {field3} {type3}
        {field4} {type4}
    }
    {TABLE1} ||--o{ {TABLE2} : "{relationship}"
```

## 数据模型

### 聚合数据模型

{aggregateDataModel}

### 领域模型映射

| 领域实体       | 数据库表      | 映射关系           |
| -------------- | ------------- | ------------------ |
| {domainEntity1} | {databaseTable1} | {mappingRelation1} |
| {domainEntity2} | {databaseTable2} | {mappingRelation2} |

## 数据分区策略

{partitioningStrategy}

## 数据归档策略

{archivingStrategy}

## 数据备份策略

{backupStrategy}

## 相关文档

- [[migration_history]] - 迁移历史
- [[dataflow]] - 数据流说明

## 变更记录

| 日期     | 版本 | 变更内容 | 变更人     |
| -------- | ---- | -------- | ---------- |
| {date}   | 1.0  | 初始版本 | {dba}      |
