# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Support for the RatioNode."""
from google.fhir.core.execution.expressions import expression_node


class RatioNode(expression_node.ExpressionNode):
  """Defines a ratio between two quantities."""

  def __init__(self=None, numerator=None, denominator=None):
    super().__init__()
    self.numerator = numerator
    self.denominator = denominator