# 📡 Plataforma Distribuída de Monitoramento e Controle de Ambientes Inteligentes

## 📝 Resumo do Projeto

Este projeto simula uma **plataforma distribuída** para **monitoramento e controle de ambientes inteligentes** (salas, laboratórios, auditórios), integrando **sensores**, **atuadores**, **Kafka**, **gRPC** e **Sockets** para comunicação em tempo real entre os componentes.

---

## 🏗️ Arquitetura do Sistema

```mermaid
graph TD
    S(Sensores) -->|UDP| G(Gateway)
    G -->|Kafka| K(Kafka)
    K --> C(Consumidor Kafka)
    C -->|gRPC| A(Armazenamento gRPC)
    G -->|TCP| T(Atuadores)
