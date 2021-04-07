FROM vault

RUN apk add --upgrade \
	libxml2 \
	libxslt \
	libxml2-dev \
	libxslt-dev \
	python3 \
	py-pip \
	python3-dev \
        groff \
        curl \
        less \
        zip \
	jq \
	alpine-sdk \
        && pip3 install --upgrade pip \
	&& pip3 install --upgrade six aws-sam-cli awscli s3cmd python-magic requests boto3 \
	&& rm /var/cache/apk/*


COPY vault_init.py /vault/entry.py
RUN chmod +x /vault/entry.py
ENTRYPOINT ["python3", "/vault/entry.py"]
