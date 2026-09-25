# An example if you do not want to use an OpenAI integration like we do in the notebook. Then you can move this to config.py as it will run as part of your "serve" command. 
# Note: you may need to tweak it depending on your setup.
# Created with help from Gemma.

# config/config.py
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

def connect_to_phoenix():
    # Fetch the tracer provider currently managed by OpenTelemetry / NeMo
    provider = trace.get_tracer_provider()

    # Define HTTP Exporter pointing to your running local Phoenix server
    exporter = OTLPSpanExporter(
        endpoint="http://127.0.0.1:6006/v1/traces"
    )
    processor = SimpleSpanProcessor(exporter)

    # Attach the Phoenix processor directly to NeMo's active provider
    if isinstance(provider, TracerProvider):
        provider.add_span_processor(processor)

connect_to_phoenix()
