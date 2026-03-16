# {serviceName} 领域概览

**创建日期**: {date:-2026-03-16}
**架构师**: {architect}
**版本**: {version:-1.0}

## 概述

本文档为 {serviceName} 微服务的**系统级领域总览**，整合领域划分、依赖与交互、子领域映射、限界上下文、基础设施与集成、共享组件及领域术语表。

---

## 领域划分

### 领域划分图

```mermaid
graph TB
    subgraph "{serviceName} 微服务"
        {domain1}[{domain1Name}]
        {domain2}[{domain2Name}]
        {domain3}[{domain3Name}]
    end

    {domain1} -->|{dependency1}| {domain2}
    {domain2} -->|{dependency2}| {domain3}
```

### 业务领域列表

| 领域名称        | 领域标识      | 职责描述               | 重要性                | 详细文档                                   |
| --------------- | ------------- | ---------------------- | --------------------- | ------------------------------------------ |
| {domain1Name}   | {domain1Id}   | {domain1Description}   | {domain1Importance}   | [[../{domain1Id}/01-module-overview.md]] |
| {domain2Name}   | {domain2Id}   | {domain2Description}   | {domain2Importance}   | [[../{domain2Id}/01-module-overview.md]] |
| {domain3Name}   | {domain3Id}   | {domain3Description}   | {domain3Importance}   | [[../{domain3Id}/01-module-overview.md]] |

---

## 领域依赖与交互

### 依赖关系图

```mermaid
graph LR
    {domain1}[{domain1Name}]
    {domain2}[{domain2Name}]
    {domain3}[{domain3Name}]

    {domain1} -->|{dependencyType1}| {domain2}
    {domain2} -->|{dependencyType2}| {domain3}
```

### 依赖关系说明

| 源领域            | 目标领域          | 依赖类型            | 依赖原因              | 交互方式               |
| ----------------- | ----------------- | ------------------- | --------------------- | ---------------------- |
| {sourceDomain1}   | {targetDomain1}   | {dependencyType1}   | {dependencyReason1}   | {interactionMethod1}   |
| {sourceDomain2}   | {targetDomain2}   | {dependencyType2}   | {dependencyReason2}   | {interactionMethod2}   |

---

## 领域术语表

> 本节为领域术语的**唯一来源**，其他文档中的术语应引用此处。

### 核心术语

| 术语      | 英文             | 定义            | 相关概念             |
| --------- | ---------------- | --------------- | -------------------- |
| {term1}   | {englishTerm1}   | {definition1}   | {relatedConcepts1}   |
| {term2}   | {englishTerm2}   | {definition2}   | {relatedConcepts2}   |
| {term3}   | {englishTerm3}   | {definition3}   | {relatedConcepts3}   |

### 领域实体

| 实体名称    | 英文               | 定义            | 属性            |
| ----------- | ------------------ | --------------- | --------------- |
| {entity1}   | {englishEntity1}   | {definition1}   | {attributes1}   |
| {entity2}   | {englishEntity2}   | {definition2}   | {attributes2}   |

### 领域值对象

| 值对象名称       | 英文                    | 定义            | 组成             |
| ---------------- | ----------------------- | --------------- | ---------------- |
| {valueObject1}   | {englishValueObject1}   | {definition1}   | {composition1}   |
| {valueObject2}   | {englishValueObject2}   | {definition2}   | {composition2}   |

### 领域事件

| 事件名称   | 英文              | 定义            | 触发条件              |
| ---------- | ----------------- | --------------- | --------------------- |
| {event1}   | {englishEvent1}   | {definition1}   | {triggerCondition1}   |
| {event2}   | {englishEvent2}   | {definition2}   | {triggerCondition2}   |

---

## 相关文档

- [[../{domain1Id}/01-module-overview.md]] - {domain1Name} 领域概览
- [[../{domain2Id}/01-module-overview.md]] - {domain2Name} 领域概览

## 变更记录

| 日期     | 版本 | 变更内容 | 变更人        |
| -------- | ---- | -------- | ------------- |
| {date}   | 1.0  | 初始版本 | {architect}   |
