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

"""Support for the QueryNode."""
from google.fhir.core.execution.expressions import expression_node


class QueryNode(expression_node.ExpressionNode):
  """The QueryNode operator represents a clause-based query."""

  def __init__(
      self=None,
      source=None,
      let=None,
      relationship=None,
      where=None,
      return_=None,
      aggregate=None,
      sort=None,
  ):
    super().__init__()
    if source is None:
      self.source = []
    else:
      self.source = source
    if let is None:
      self.let = []
    else:
      self.let = let
    if relationship is None:
      self.relationship = []
    else:
      self.relationship = relationship
    self.where = where
    self.return_ = return_
    self.aggregate = aggregate
    self.sort = sort