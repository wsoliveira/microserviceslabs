# Laboratorio Para testar MicroServicos Python, Docker e K8s


## APP's

 - cadastro (fastapi/sqlite)
 - recurso (flask/sqlite)
 - scripts_asynciolabs (scripts assincronos e paralelismo com threads e process)

## DOCKER-COMPOSE
 
 - Rabbit
 - MongoDB
 - APP's citados acima

 ## K8S
   - minikube start (subir o minikube)
   - kubectl get pods -A (verificar pods)  
   - kubectl get services -A (verificar os serviços no AR)
   - kubectl create namespace microserviceslabs (criar namespace)
   - kubectl apply -f ./appcadastro/ (criar/alterar pods e services)
   - kubectl describe pod appcadastro-deployment --namespace microserviceslabs
   - kubectl port-forward --namespace microserviceslabs svc/appcadastro-service 8010:8010 (para acessar o microservico)
   - kubectl apply -f ./asynciolabs/ (criando job e cronjobs para execucao de scripts no kubernetes)

## K8S - Rabbitmq
   - helm repo add bitnami https://charts.bitnami.com/bitnami

   - helm install rabbitmq --set rabbitmq.username=admin,rabbitmq.password=123mudar,persistence.size=1Gi stable/rabbitmq --namespace microserviceslabs
   - kubectl port-forward --namespace microserviceslabs svc/rabbitmq 15672:15672


   https://eduardomatos.dev/deployando-microsservicos-com-rabbitmq-e-mongodb-no-kubernetes/
   https://artifacthub.io/packages/helm/bitnami/rabbitmq/6.8.4
   #https://phoenixnap.com/kb/install-and-configure-rabbitmq-on-kubernetes

## TODO
 - Subir para GIT
 - Criar k8s
 - Celery no app recurso
    - https://testdriven.io/blog/fastapi-mongo/
 - Add mongodb no app cadastro




## License
[MIT](https://choosealicense.com/licenses/mit/)