gen_proto:
	python -m grpc_tools.protoc -I./proto \
		--python_out=./lib --grpc_python_out=./lib ./proto/*.proto
	sed -i -E 's/^(import.*_pb2)/from . \1/' lib/*.py
