# {serviceName} 威胁建模

**创建日期**: {date:-2026-03-16}
**安全工程师**: {securityEngineer}
**版本**: {version:-1.0}

## 概述

本文档使用 STRIDE 模型对 {serviceName} 微服务进行威胁建模（Threat Modeling）。

## STRIDE 模型

### STRIDE 定义

- **S**poofing（伪装）: {spoofingDefinition}
- **T**ampering（篡改）: {tamperingDefinition}
- **R**epudiation（否认）: {repudiationDefinition}
- **I**nformation Disclosure（信息泄露）: {informationDisclosureDefinition}
- **D**enial of Service（拒绝服务）: {denialOfServiceDefinition}
- **E**levation of Privilege（权限提升）: {elevationOfPrivilegeDefinition}

## 威胁分析

### Spoofing（伪装）

#### 威胁描述

{spoofingThreatDescription}

#### 缓解措施

{spoofingMitigation}

### Tampering（篡改）

#### 威胁描述

{tamperingThreatDescription}

#### 缓解措施

{tamperingMitigation}

### Information Disclosure（信息泄露）

#### 威胁描述

{informationDisclosureThreatDescription}

#### 缓解措施

{informationDisclosureMitigation}

### Denial of Service（拒绝服务）

#### 威胁描述

{denialOfServiceThreatDescription}

#### 缓解措施

{denialOfServiceMitigation}

### Elevation of Privilege（权限提升）

#### 威胁描述

{elevationOfPrivilegeThreatDescription}

#### 缓解措施

{elevationOfPrivilegeMitigation}

## 威胁矩阵

| 威胁类型     | 威胁等级       | 可能性      | 影响        | 风险等级       | 缓解措施       |
| ------------ | -------------- | ----------- | ----------- | -------------- | -------------- |
| {threat1}    | {threatLevel1} | {likelihood1} | {impact1}    | {riskLevel1}   | {mitigation1}  |
| {threat2}    | {threatLevel2} | {likelihood2} | {impact2}    | {riskLevel2}   | {mitigation2}  |

## 安全控制措施

### 预防性控制

{preventiveControls}

### 检测性控制

{detectiveControls}

### 纠正性控制

{correctiveControls}

## 相关文档

- [[authz_authn]] - 鉴权认证策略
- [[data_protection]] - 数据保护
- [[audit]] - 审计日志规范

## 变更记录

| 日期     | 版本 | 变更内容 | 变更人               |
| -------- | ---- | -------- | -------------------- |
| {date}   | 1.0  | 初始版本 | {securityEngineer}   |
