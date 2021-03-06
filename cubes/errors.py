"""Exceptions used in Cubes.

The base exception calss is :class:`.CubesError`."""

class CubesError(Exception):
    """Generic error class."""

class UserError(CubesError):
    """Superclass for all errors caused by the cubes and slicer users. Error
    messages from this error might be safely passed to the front-end. Do not
    include any information that you would not like to be public"""

class InternalError(CubesError):
    """Superclass for all errors that happened internally: configuration
    issues, connection problems, model inconsistencies..."""

class ConfigurationError(InternalError):
    """Raised when there is a problem with workspace configuration assumed."""

class BackendError(InternalError):
    """Raised by a backend. Should be handled separately, for example: should
    not be passed to the client from the server due to possible internal
    schema exposure.
    """

class WorkspaceError(InternalError):
    """Backend Workspace related exception."""

class BrowserError(InternalError):
    """AggregationBrowser related exception."""
    pass

class ModelError(InternalError):
    """Model related exception."""

# TODO: necessary? or rename to PhysicalModelError
class MappingError(ModelError):
    """Raised when there are issues by mapping from logical model to physical
    database schema. """


# TODO: change all instances to ModelError
class ModelInconsistencyError(ModelError):
    """Raised when there is incosistency in model structure."""

class TemplateRequired(ModelError):
    """Raised by a model provider which can provide a dimension, but requires
    a template. Signals to the caller that the creation of a dimension should
    be retried when the template is available."""

    def __init__(self, template):
        self.template = template
    def __str__(self):
        return self.template

class MissingObjectError(UserError):
    def __init__(self, message=None, name=None):
        self.name = name
        self.message = message

    def __str__(self):
        return self.message or self.name

class NoSuchDimensionError(MissingObjectError):
    """Raised when an unknown dimension is requested."""

class NoSuchCubeError(MissingObjectError):
    """Raised when an unknown cube is requested."""

class NoSuchAttributeError(UserError):
    """Raised when an unknown attribute, measure or detail requested."""

class ArgumentError(UserError):
    """Raised when an invalid or conflicting function argument is supplied.
    """

class HierarchyError(UserError):
    """Raised when attemt to get level deeper than deepest level in a
    hierarchy"""

