# Proyecto semestral Gestión de Proyectos de Software
Proyecto desarrollado por Matías Guiñez Monsalve y José García Navarrete estudiantes de la Universidad del Bío-Bío.

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [DevOps](#devops)

## Descripción
Este proyecto se realizó como parte del curso de Gestión de Proyectos de Software. El objetivo principal es desarrollar una aplicación la cual siga la filosofía DevOps, con el fin de generar una integración y despliegue continuo.

## DevOps
Para asegurar un ciclo de vida de desarrollo de software eficiente y de alta calidad, se implementaron las siguientes prácticas y herramientas de DevOps:

![DevOps Pipeline](./devops.png)

<img src="./devops.png" alt="DevOps Pipeline" width="600"/>

### Integración Continua (CI)
Se utilizó GitHub Actions para configurar la integración continua. Cada vez que se realiza un commit, se ejecutan automáticamente las pruebas unitarias para garantizar que no se introduzcan errores en el código base.

### Despliegue Continuo (CD)
El despliegue continuo se configuró utilizando Vercel.

### Monitorización y Loggin
Se implementaron herramientas como Prometheus y Grafana para la monitorización del rendimiento y la salud de la aplicación, así como ELK Stack (Elasticsearch, Logstash, Kibana) para la gestión de logs.

### Pipeline CI/CD
El pipeline CI/CD consta de los siguientes pasos:
1. **Build**: Construcción de la aplicación.
2. **Test**: Ejecución de los tests.
3. **Deploy**: Despliegue de la apliación atraves de Vercel.
4. **Monitor**: Monitorización continua del rendimiento y la salud de la aplicación.
