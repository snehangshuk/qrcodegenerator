.PHONY: update
update:  
    @eval $$(minikube docker-env) ;\
    docker image build -t python-qrcode:v1 -f Dockerfile .
    kubectl set image deployment/python-qrcode *=python-qrcode:v1
