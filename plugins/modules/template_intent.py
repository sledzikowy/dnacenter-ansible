#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Ansible module to perform operations on project and templates in DNAC."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Madhan Sankaranarayanan, Rishita Chowdhary']

DOCUMENTATION = r"""
---
module: template_intent
short_description: Resource module for Template functions
description:
- Manage operations create, update and delete of the resource Configuration Template.
- API to create a template by project name and template name.
- API to update a template by template name and project name.
- API to delete a template by template name and project name.
- API to export the projects for given projectNames.
- API to export the templates for given templateIds.
- API to manage operation create of the resource Configuration Template Import Project.
- API to manage operation create of the resource Configuration Template Import Template.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Akash Bhaskaran (@akabhask)
        Muthu Rakesh (@MUTHU-RAKESH-27)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of templates being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      configuration_templates:
        description: Create/Update/Delete template.
        type: dict
        suboptions:
          author:
            description: Author of template.
            type: str
          composite:
            description: Is it composite template.
            type: bool
          containing_templates:
            description: Configuration Template Create's containingTemplates.
            suboptions:
              composite:
                description: Is it composite template.
                type: bool
              description:
                description: Description of template.
                type: str
              device_types:
                description: deviceTypes on which templates would be applied.
                type: list
                elements: dict
                suboptions:
                  productFamily:
                    description: Device family.
                    type: str
                  productSeries:
                    description: Device series.
                    type: str
                  productType:
                    description: Device type.
                    type: str
              id:
                description: UUID of template.
                type: str
              language:
                description: Template language
                choices:
                  - JINJA
                  - VELOCITY
                type: str
              name:
                description: Name of template.
                type: str
              project_name:
                description: Name of the project under which templates are managed.
                type: str
              projectDescription:
                description: Description of the project created.
                type: str
              rollbackTemplateParams:
                description: Params required for template rollback.
                type: list
                elements: dict
                suboptions:
                  binding:
                    description: Bind to source.
                    type: str
                  customOrder:
                    description: CustomOrder of template param.
                    type: int
                  dataType:
                    description: Datatype of template param.
                    type: str
                  defaultValue:
                    description: Default value of template param.
                    type: str
                  description:
                    description: Description of template param.
                    type: str
                  displayName:
                    description: Display name of param.
                    type: str
                  group:
                    description: Group.
                    type: str
                  id:
                    description: UUID of template param.
                    type: str
                  instructionText:
                    description: Instruction text for param.
                    type: str
                  key:
                    description: Key.
                    type: str
                  notParam:
                    description: Is it not a variable.
                    type: bool
                  order:
                    description: Order of template param.
                    type: int
                  paramArray:
                    description: Is it an array.
                    type: bool
                  parameterName:
                    description: Name of template param.
                    type: str
                  provider:
                    description: Provider.
                    type: str
                  range:
                    description: Configuration Template Create's range.
                    type: list
                    elements: dict
                    suboptions:
                      id:
                        description: UUID of range.
                        type: str
                      maxValue:
                        description: Max value of range.
                        type: int
                      minValue:
                        description: Min value of range.
                        type: int
                  required:
                    description: Is param required.
                    type: bool
                  selection:
                    description: Configuration Template Create's selection.
                    suboptions:
                      defaultSelectedValues:
                        description: Default selection values.
                        elements: str
                        type: list
                      id:
                        description: UUID of selection.
                        type: str
                      selectionType:
                        description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                        type: str
                      selectionValues:
                        description: Selection values.
                        type: dict
                    type: dict
              tags:
                description: Configuration Template Create's tags.
                suboptions:
                  id:
                    description: UUID of tag.
                    type: str
                  name:
                    description: Name of tag.
                    type: str
                type: list
                elements: dict
              template_content:
                description: Template content.
                type: str
              templateParams:
                description: Configuration Template Create's templateParams.
                elements: dict
                suboptions:
                  binding:
                    description: Bind to source.
                    type: str
                  customOrder:
                    description: CustomOrder of template param.
                    type: int
                  dataType:
                    description: Datatype of template param.
                    type: str
                  defaultValue:
                    description: Default value of template param.
                    type: str
                  description:
                    description: Description of template param.
                    type: str
                  displayName:
                    description: Display name of param.
                    type: str
                  group:
                    description: Group.
                    type: str
                  id:
                    description: UUID of template param.
                    type: str
                  instructionText:
                    description: Instruction text for param.
                    type: str
                  key:
                    description: Key.
                    type: str
                  notParam:
                    description: Is it not a variable.
                    type: bool
                  order:
                    description: Order of template param.
                    type: int
                  paramArray:
                    description: Is it an array.
                    type: bool
                  parameterName:
                    description: Name of template param.
                    type: str
                  provider:
                    description: Provider.
                    type: str
                  range:
                    description: Configuration Template Create's range.
                    suboptions:
                      id:
                        description: UUID of range.
                        type: str
                      maxValue:
                        description: Max value of range.
                        type: int
                      minValue:
                        description: Min value of range.
                        type: int
                    type: list
                    elements: dict
                  required:
                    description: Is param required.
                    type: bool
                  selection:
                    description: Configuration Template Create's selection.
                    suboptions:
                      defaultSelectedValues:
                        description: Default selection values.
                        elements: str
                        type: list
                      id:
                        description: UUID of selection.
                        type: str
                      selectionType:
                        description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                        type: str
                      selectionValues:
                        description: Selection values.
                        type: dict
                    type: dict
                type: list
              version:
                description: Current version of template.
                type: str
            type: list
            elements: dict
          create_time:
            description: Create time of template.
            type: int
          custom_params_order:
            description: Custom Params Order.
            type: bool
          template_description:
            description: Description of template.
            type: str
          device_types:
            description: Configuration Template Create's deviceTypes. This field is mandatory to create a new template.
            suboptions:
              productFamily:
                description: Device family.
                type: str
              productSeries:
                description: Device series.
                type: str
              productType:
                description: Device type.
                type: str
            type: list
            elements: dict
          failure_policy:
            description: Define failure policy if template provisioning fails.
            type: str
          language:
            description: Template language
            choices:
              - JINJA
              - VELOCITY
            type: str
          last_update_time:
            description: Update time of template.
            type: int
          latest_version_time:
            description: Latest versioned template time.
            type: int
          template_name:
            description: Name of template. This field is mandatory to create a new template.
            type: str
          parent_template_id:
            description: Parent templateID.
            type: str
          project_id:
            description: Project UUID.
            type: str
          project_name:
            description: Project name.
            type: str
          projectDescription:
            description: Project Description.
            type: str
          rollback_template_content:
            description: Rollback template content.
            type: str
          rollback_template_params:
            description: Configuration Template Create's rollbackTemplateParams.
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
                type: list
                elements: dict
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                    elements: str
                    type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
            type: list
            elements: dict
          software_type:
            description: Applicable device software type. This field is mandatory to create a new template.
            type: str
          software_variant:
            description: Applicable device software variant.
            type: str
          software_version:
            description: Applicable device software version.
            type: str
          template_tag:
            description: Configuration Template Create's tags.
            suboptions:
              id:
                description: UUID of tag.
                type: str
              name:
                description: Name of tag.
                type: str
            type: list
            elements: dict
          template_content:
            description: Template content.
            type: str
          template_params:
            description: Configuration Template Create's templateParams.
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
                type: list
                elements: dict
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                    elements: str
                    type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
            type: list
            elements: dict
          validation_errors:
            description: Configuration Template Create's validationErrors.
            suboptions:
              rollbackTemplateErrors:
                description: Validation or design conflicts errors of rollback template.
                elements: dict
                type: list
              templateErrors:
                description: Validation or design conflicts errors.
                elements: dict
                type: list
              templateId:
                description: UUID of template.
                type: str
              templateVersion:
                description: Current version of template.
                type: str
            type: dict
          version:
            description: Current version of template.
            type: str
          version_description:
            description: Template version comments.
            type: str
      export:
        description: Export the project/template details.
        type: dict
        suboptions:
          project:
            description: Export the project.
            type: list
            elements: str
          template:
            description: Export the template.
            type: list
            elements: dict
            suboptions:
              project_name:
                description: Name of the project under the template available.
                type: str
              template_name:
                description: Name of the template which we need to export
                type: str
      import:
        description: Import the project/template details.
        type:
        suboptions:
          project:
            description: Import the project details.
            type: dict
            suboptions:
              doVersion:
                description: DoVersion query parameter. If this flag is true, creates a new
                  version of the template with the imported contents, if the templates already
                  exists. " If false and if template already exists, then operation
                  fails with 'Template already exists' error.
                type: bool
          template:
            description: Import the template details.
            type: dict
            suboptions:
              doVersion:
                description: DoVersion query parameter. If this flag is true, creates a new
                  version of the template with the imported contents, if the templates already
                  exists. " If false and if template already exists, then operation
                  fails with 'Template already exists' error.
                type: bool
              payload:
                description: Configuration Template Import Template's payload.
                elements: dict
                suboptions:
                  author:
                    description: Author of template.
                    type: str
                  composite:
                    description: Is it composite template.
                    type: bool
                  containingTemplates:
                    description: Configuration Template Import Template's containingTemplates.
                    elements: dict
                    suboptions:
                      composite:
                        description: Is it composite template.
                        type: bool
                      description:
                        description: Description of template.
                        type: str
                      device_types:
                        description: Configuration Template Import Template's deviceTypes.
                        elements: dict
                        suboptions:
                          productFamily:
                            description: Device family.
                            type: str
                          productSeries:
                            description: Device series.
                            type: str
                          productType:
                            description: Device type.
                            type: str
                        type: list
                      id:
                        description: UUID of template.
                        type: str
                      language:
                        description: Template language (JINJA or VELOCITY).
                        type: str
                      name:
                        description: Name of template.
                        type: str
                      project_name:
                        description: Project name.
                        type: str
                      rollbackTemplateParams:
                        description: Configuration Template Import Template's rollbackTemplateParams.
                        elements: dict
                        suboptions:
                          binding:
                            description: Bind to source.
                            type: str
                          customOrder:
                            description: CustomOrder of template param.
                            type: int
                          dataType:
                            description: Datatype of template param.
                            type: str
                          defaultValue:
                            description: Default value of template param.
                            type: str
                          description:
                            description: Description of template param.
                            type: str
                          displayName:
                            description: Display name of param.
                            type: str
                          group:
                            description: Group.
                            type: str
                          id:
                            description: UUID of template param.
                            type: str
                          instructionText:
                            description: Instruction text for param.
                            type: str
                          key:
                            description: Key.
                            type: str
                          notParam:
                            description: Is it not a variable.
                            type: bool
                          order:
                            description: Order of template param.
                            type: int
                          paramArray:
                            description: Is it an array.
                            type: bool
                          parameterName:
                            description: Name of template param.
                            type: str
                          provider:
                            description: Provider.
                            type: str
                          range:
                            description: Configuration Template Import Template's range.
                            elements: dict
                            suboptions:
                              id:
                                description: UUID of range.
                                type: str
                              maxValue:
                                description: Max value of range.
                                type: int
                              minValue:
                                description: Min value of range.
                                type: int
                            type: list
                          required:
                            description: Is param required.
                            type: bool
                          selection:
                            description: Configuration Template Import Template's selection.
                            suboptions:
                              defaultSelectedValues:
                                description: Default selection values.
                                elements: str
                                type: list
                              id:
                                description: UUID of selection.
                                type: str
                              selectionType:
                                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                                type: str
                              selectionValues:
                                description: Selection values.
                                type: dict
                            type: dict
                        type: list
                      tags:
                        description: Configuration Template Import Template's tags.
                        elements: dict
                        suboptions:
                          id:
                            description: UUID of tag.
                            type: str
                          name:
                            description: Name of tag.
                            type: str
                        type: list
                      template_content:
                        description: Template content.
                        type: str
                      templateParams:
                        description: Configuration Template Import Template's templateParams.
                        elements: dict
                        suboptions:
                          binding:
                            description: Bind to source.
                            type: str
                          customOrder:
                            description: CustomOrder of template param.
                            type: int
                          dataType:
                            description: Datatype of template param.
                            type: str
                          defaultValue:
                            description: Default value of template param.
                            type: str
                          description:
                            description: Description of template param.
                            type: str
                          displayName:
                            description: Display name of param.
                            type: str
                          group:
                            description: Group.
                            type: str
                          id:
                            description: UUID of template param.
                            type: str
                          instructionText:
                            description: Instruction text for param.
                            type: str
                          key:
                            description: Key.
                            type: str
                          notParam:
                            description: Is it not a variable.
                            type: bool
                          order:
                            description: Order of template param.
                            type: int
                          paramArray:
                            description: Is it an array.
                            type: bool
                          parameterName:
                            description: Name of template param.
                            type: str
                          provider:
                            description: Provider.
                            type: str
                          range:
                            description: Configuration Template Import Template's range.
                            elements: dict
                            suboptions:
                              id:
                                description: UUID of range.
                                type: str
                              maxValue:
                                description: Max value of range.
                                type: int
                              minValue:
                                description: Min value of range.
                                type: int
                            type: list
                          required:
                            description: Is param required.
                            type: bool
                          selection:
                            description: Configuration Template Import Template's selection.
                            suboptions:
                              defaultSelectedValues:
                                description: Default selection values.
                                elements: str
                                type: list
                              id:
                                description: UUID of selection.
                                type: str
                              selectionType:
                                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                                type: str
                              selectionValues:
                                description: Selection values.
                                type: dict
                            type: dict
                        type: list
                      version:
                        description: Current version of template.
                        type: str
                    type: list
                  createTime:
                    description: Create time of template.
                    type: int
                  customParamsOrder:
                    description: Custom Params Order.
                    type: bool
                  description:
                    description: Description of template.
                    type: str
                  device_types:
                    description: Configuration Template Import Template's deviceTypes.
                    elements: dict
                    suboptions:
                      productFamily:
                        description: Device family.
                        type: str
                      productSeries:
                        description: Device series.
                        type: str
                      productType:
                        description: Device type.
                        type: str
                    type: list
                  failurePolicy:
                    description: Define failure policy if template provisioning fails.
                    type: str
                  id:
                    description: UUID of template.
                    type: str
                  language:
                    description: Template language (JINJA or VELOCITY).
                    type: str
                  lastUpdateTime:
                    description: Update time of template.
                    type: int
                  latestVersionTime:
                    description: Latest versioned template time.
                    type: int
                  name:
                    description: Name of template.
                    type: str
                  parentTemplateId:
                    description: Parent templateID.
                    type: str
                  projectId:
                    description: Project UUID.
                    type: str
                  project_name:
                    description: Project name.
                    type: str
                  rollbackTemplateContent:
                    description: Rollback template content.
                    type: str
                  rollbackTemplateParams:
                    description: Configuration Template Import Template's rollbackTemplateParams.
                    elements: dict
                    suboptions:
                      binding:
                        description: Bind to source.
                        type: str
                      customOrder:
                        description: CustomOrder of template param.
                        type: int
                      dataType:
                        description: Datatype of template param.
                        type: str
                      defaultValue:
                        description: Default value of template param.
                        type: str
                      description:
                        description: Description of template param.
                        type: str
                      displayName:
                        description: Display name of param.
                        type: str
                      group:
                        description: Group.
                        type: str
                      id:
                        description: UUID of template param.
                        type: str
                      instructionText:
                        description: Instruction text for param.
                        type: str
                      key:
                        description: Key.
                        type: str
                      notParam:
                        description: Is it not a variable.
                        type: bool
                      order:
                        description: Order of template param.
                        type: int
                      paramArray:
                        description: Is it an array.
                        type: bool
                      parameterName:
                        description: Name of template param.
                        type: str
                      provider:
                        description: Provider.
                        type: str
                      range:
                        description: Configuration Template Import Template's range.
                        elements: dict
                        suboptions:
                          id:
                            description: UUID of range.
                            type: str
                          maxValue:
                            description: Max value of range.
                            type: int
                          minValue:
                            description: Min value of range.
                            type: int
                        type: list
                      required:
                        description: Is param required.
                        type: bool
                      selection:
                        description: Configuration Template Import Template's selection.
                        suboptions:
                          defaultSelectedValues:
                            description: Default selection values.
                            elements: str
                            type: list
                          id:
                            description: UUID of selection.
                            type: str
                          selectionType:
                            description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                            type: str
                          selectionValues:
                            description: Selection values.
                            type: dict
                        type: dict
                    type: list
                  software_type:
                    description: Applicable device software type.
                    type: str
                  software_variant:
                    description: Applicable device software variant.
                    type: str
                  softwareVersion:
                    description: Applicable device software version.
                    type: str
                  tags:
                    description: Configuration Template Import Template's tags.
                    elements: dict
                    suboptions:
                      id:
                        description: UUID of tag.
                        type: str
                      name:
                        description: Name of tag.
                        type: str
                    type: list
                  template_content:
                    description: Template content.
                    type: str
                  templateParams:
                    description: Configuration Template Import Template's templateParams.
                    elements: dict
                    suboptions:
                      binding:
                        description: Bind to source.
                        type: str
                      customOrder:
                        description: CustomOrder of template param.
                        type: int
                      dataType:
                        description: Datatype of template param.
                        type: str
                      defaultValue:
                        description: Default value of template param.
                        type: str
                      description:
                        description: Description of template param.
                        type: str
                      displayName:
                        description: Display name of param.
                        type: str
                      group:
                        description: Group.
                        type: str
                      id:
                        description: UUID of template param.
                        type: str
                      instructionText:
                        description: Instruction text for param.
                        type: str
                      key:
                        description: Key.
                        type: str
                      notParam:
                        description: Is it not a variable.
                        type: bool
                      order:
                        description: Order of template param.
                        type: int
                      paramArray:
                        description: Is it an array.
                        type: bool
                      parameterName:
                        description: Name of template param.
                        type: str
                      provider:
                        description: Provider.
                        type: str
                      range:
                        description: Configuration Template Import Template's range.
                        elements: dict
                        suboptions:
                          id:
                            description: UUID of range.
                            type: str
                          maxValue:
                            description: Max value of range.
                            type: int
                          minValue:
                            description: Min value of range.
                            type: int
                        type: list
                      required:
                        description: Is param required.
                        type: bool
                      selection:
                        description: Configuration Template Import Template's selection.
                        suboptions:
                          defaultSelectedValues:
                            description: Default selection values.
                            elements: str
                            type: list
                          id:
                            description: UUID of selection.
                            type: str
                          selectionType:
                            description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                            type: str
                          selectionValues:
                            description: Selection values.
                            type: dict
                        type: dict
                    type: list
                  validationErrors:
                    description: Configuration Template Import Template's validationErrors.
                    suboptions:
                      rollbackTemplateErrors:
                        description: Validation or design conflicts errors of rollback template.
                        type: dict
                      templateErrors:
                        description: Validation or design conflicts errors.
                        type: dict
                      templateId:
                        description: UUID of template.
                        type: str
                      templateVersion:
                        description: Current version of template.
                        type: str
                    type: dict
                  version:
                    description: Current version of template.
                    type: str
                type: list
              project_name:
                description: ProjectName path parameter. Project name to create template under the
                  project.
                type: str

requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template,
    configuration_templates.ConfigurationTemplates.deletes_the_template,
    configuration_templates.ConfigurationTemplates.update_template,
    configuration_templates.ConfigurationTemplates.export_projects,
    configuration_templates.ConfigurationTemplates.export_templates,
    configuration_templates.ConfigurationTemplates.imports_the_projects_provided,
    configuration_templates.ConfigurationTemplates.imports_the_templates_provided,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/project/{projectId}/template,
    delete /dna/intent/api/v1/template-programmer/template/{templateId},
    put /dna/intent/api/v1/template-programmer/template,
    post /dna/intent/api/v1/template-programmer/project/name/exportprojects,
    post /dna/intent/api/v1/template-programmer/template/exporttemplates,
    post /dna/intent/api/v1/template-programmer/project/importprojects,
    post /dna/intent/api/v1/template-programmer/project/name/{projectName}/template/importtemplates,

"""

EXAMPLES = r"""
- name: Create a new template, export and import the project and template.
  cisco.dnac.template_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
    - configuration_templates:
        author: string
        composite: true
        create_time: 0
        custom_params_order: true
        description: string
        device_types:
        - productFamily: string
          productSeries: string
          productType: string
        failure_policy: string
        id: string
        language: string
        last_update_time: 0
        latest_version_time: 0
        name: string
        parent_template_id: string
        project_id: string
        project_name: string
        project_description: string
        rollback_template_content: string
        software_type: string
        software_variant: string
        software_version: string
        tags:
        - id: string
          name: string
        template_content: string
        validation_errors:
            rollbackTemplateErrors:
            - {}
            templateErrors:
            - {}
            templateId: string
            templateVersion: string
        version: string
      export:
        project:
          - string
        template:
          - project_name : string
            template_name: string
      import:
        project:
          doVersion: true
        export:
          doVersion: true
          payload:
          - author: string
            composite: true
            containingTemplates:
            - composite: true
              description: string
              device_types:
              - productFamily: string
                productSeries: string
                productType: string
              id: string
              language: string
              name: string
              project_name: string
              rollbackTemplateParams:
              - binding: string
                customOrder: 0
                dataType: string
                defaultValue: string
                description: string
                displayName: string
                group: string
                id: string
                instructionText: string
                key: string
                notParam: true
                order: 0
                paramArray: true
                parameterName: string
                provider: string
                range:
                - id: string
            project_name: string


"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of template/project
response_1:
  description: A dictionary with versioning details of the template as returned by the DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
                        "endTime": 0,
                        "version": 0,
                        "data": String,
                        "startTime": 0,
                        "username": String,
                        "progress": String,
                        "serviceType": String, "rootId": String,
                        "isError": bool,
                        "instanceTenantId": String,
                        "id": String
                        "version": 0
                  },
      "msg": String
    }

# Case_2: Error while deleting a template or when given project is not found
response_2:
  description: A list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

# Case_3: Given template already exists and requires no update
response_3:
  description: A dictionary with the exisiting template deatails as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

# Case_4: Given template list that needs to be exported
response_4:
  description: Details of the templates in the list as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

# Case_5: Given project list that needs to be exported
response_5:
  description: Details of the projects in the list as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class DnacTemplate(DnacBase):
    """Class containing member attributes for template intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.have_project = {}
        self.have_template = {}
        self.supported_states = ["merged", "deleted"]
        self.accepted_languages = ["JINJA", "VELOCITY"]
        self.export_template = []
        self.result['response'].append({})

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed',
            'self.msg' will describe the validation issues.

        """

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = {
            "configuration_templates": {
                'type': 'dict',
                'tags': {'type': 'list'},
                'author': {'type': 'str'},
                'composite': {'type': 'bool'},
                'containing_templates': {'type': 'list'},
                'create_time': {'type': 'int'},
                'custom_params_order': {'type': 'bool'},
                'description': {'type': 'str'},
                'device_types': {
                    'type': 'list',
                    'elements': 'dict',
                    'productFamily': {'type': 'str'},
                    'productSeries': {'type': 'str'},
                    'productType': {'type': 'str'},
                },
                'failure_policy': {'type': 'str'},
                'id': {'type': 'str'},
                'language': {'type': 'str'},
                'last_update_time': {'type': 'int'},
                'latest_version_time': {'type': 'int'},
                'name': {'type': 'str'},
                'parent_template_id': {'type': 'str'},
                'project_id': {'type': 'str'},
                'project_name': {'type': 'str'},
                'project_description': {'type': 'str'},
                'rollback_template_content': {'type': 'str'},
                'rollback_template_params': {'type': 'list'},
                'software_type': {'type': 'str'},
                'software_variant': {'type': 'str'},
                'software_version': {'type': 'str'},
                'template_content': {'type': 'str'},
                'template_params': {'type': 'list'},
                'template_name': {'type': 'str'},
                'validation_errors': {'type': 'dict'},
                'version': {'type': 'str'},
                'version_description': {'type': 'str'}
            },
            'export': {
                'type': 'dict',
                'project': {'type': 'list', 'elements': 'str'},
                'template': {
                    'type': 'list',
                    'elements': 'dict',
                    'project_name': {'type': 'str'},
                    'template_name': {'type': 'str'}
                }
            },
            'import': {
                'type': 'dict',
                'project': {
                    'type': 'dict',
                    'do_version': {'type': 'str', 'default': 'False'},
                },
                'template': {
                    'type': 'dict',
                    'do_version': {'type': 'str', 'default': 'False'},
                    'payload': {
                        'type': 'list',
                        'elements': 'dict',
                        'tags': {'type': 'list'},
                        'author': {'type': 'str'},
                        'composite': {'type': 'bool'},
                        'containingTemplates': {'type': 'list'},
                        'createTime': {'type': 'int'},
                        'customParamsOrder': {'type': 'bool'},
                        'description': {'type': 'str'},
                        'device_types': {
                            'type': 'list',
                            'elements': 'dict',
                            'productFamily': {'type': 'str'},
                            'productSeries': {'type': 'str'},
                            'productType': {'type': 'str'},
                        },
                        'failurePolicy': {'type': 'str'},
                        'id': {'type': 'str'},
                        'language': {'type': 'str'},
                        'lastUpdateTime': {'type': 'int'},
                        'latestVersionTime': {'type': 'int'},
                        'name': {'type': 'str'},
                        'parentTemplateId': {'type': 'str'},
                        'projectId': {'type': 'str'},
                        'project_name': {'type': 'str'},
                        'projectDescription': {'type': 'str'},
                        'rollbackTemplateContent': {'type': 'str'},
                        'rollbackTemplateParams': {'type': 'list'},
                        'software_type': {'type': 'str'},
                        'software_variant': {'type': 'str'},
                        'softwareVersion': {'type': 'str'},
                        'template_content': {'type': 'str'},
                        'templateParams': {'type': 'list'},
                        'template_name': {'type': 'str'},
                        'validationErrors': {'type': 'dict'},
                        'version': {'type': 'str'}
                    }
                }
            }
        }
        # Validate template params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_project_params(self, params):
        """
        Store project parameters from the playbook for template processing in DNAC.

        Parameters:
            params (dict) - Playbook details containing Project information.

        Returns:
            project_params (dict) - Organized Project parameters.
        """

        configuration_templates = params.get("configuration_templates")
        project_params = {"name": configuration_templates.get("project_name"),
                          "description": configuration_templates.get("project_description")
                          }
        return project_params

    def get_template_params(self, params):
        """
        Store template parameters from the playbook for template processing in DNAC.

        Parameters:
            params (dict) - Playbook details containing Template information.

        Returns:
            temp_params (dict) - Organized template parameters.
        """

        configuration_templates = params.get("configuration_templates")
        temp_params = {
            "tags": configuration_templates.get("template_tag"),
            "author": configuration_templates.get("author"),
            "composite": configuration_templates.get("composite"),
            "containingTemplates": configuration_templates.get("containing_templates"),
            "createTime": configuration_templates.get("create_time"),
            "customParamsOrder": configuration_templates.get("custom_params_order"),
            "description": configuration_templates.get("template_description"),
            "deviceTypes": configuration_templates.get("device_types"),
            "failurePolicy": configuration_templates.get("failure_policy"),
            "id": configuration_templates.get("templateId"),
            "language": configuration_templates.get("language").upper(),
            "lastUpdateTime": configuration_templates.get("last_update_time"),
            "latestVersionTime": configuration_templates.get("latest_version_time"),
            "name": configuration_templates.get("template_name"),
            "parentTemplateId": configuration_templates.get("parent_template_id"),
            "projectId": configuration_templates.get("project_id"),
            "projectName": configuration_templates.get("project_name"),
            "rollbackTemplateContent": configuration_templates.get("rollback_template_content"),
            "rollbackTemplateParams": configuration_templates.get("rollback_template_params"),
            "softwareType": configuration_templates.get("software_type"),
            "softwareVariant": configuration_templates.get("software_variant"),
            "softwareVersion": configuration_templates.get("software_version"),
            "templateContent": configuration_templates.get("template_content"),
            "templateParams": configuration_templates.get("template_params"),
            "validationErrors": configuration_templates.get("validation_errors"),
            "version": configuration_templates.get("version"),
            "project_id": configuration_templates.get("project_id"),
        }
        return temp_params

    def get_template(self, config):
        """
        Get the template needed for updation or creation.

        Parameters:
            config (dict) - Playbook details containing Template information.

        Returns:
            result (dict) - Template details for the given template ID.
        """

        result = None
        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function="get_template_details",
            params={"template_id": config.get("templateId")}
        )
        if items:
            result = items

        self.log(str(items))
        self.result['response'] = items
        return result

    def get_have_project(self, config):
        """
        Get the current project related information from DNAC.

        Parameters:
            config (dict) - Playbook details containing Project information.

        Returns:
            template_available (list) - Current project information.
        """

        have_project = {}
        given_projectName = config.get("configuration_templates").get("project_name")
        template_available = None

        # Check if project exists.
        project_details = self.get_project_details(given_projectName)
        # DNAC returns project details even if the substring matches.
        # Hence check the projectName retrieved from DNAC.
        if not (project_details and isinstance(project_details, list)):
            self.log("Project: {0} not found, need to create new project in DNAC"
                     .format(given_projectName))
            return None

        fetched_projectName = project_details[0].get('name')
        if fetched_projectName != given_projectName:
            self.log("Project {0} provided is not exact match in DNAC DB"
                     .format(given_projectName))
            return None

        template_available = project_details[0].get('templates')
        have_project["project_found"] = True
        have_project["id"] = project_details[0].get("id")
        have_project["isDeletable"] = project_details[0].get("isDeletable")

        self.have_project = have_project
        return template_available

    def get_have_template(self, config, template_available):
        """
        Get the current template related information from DNAC.

        Parameters:
            config (dict) - Playbook details containing Template information.
            template_available (list) -  Current project information.

        Returns:
            self
        """

        projectName = config.get("configuration_templates").get("project_name")
        templateName = config.get("configuration_templates").get("template_name")
        template = None
        have_template = {}

        have_template["isCommitPending"] = False
        have_template["template_found"] = False

        template_details = get_dict_result(template_available,
                                           "name",
                                           templateName)
        # Check if specified template in playbook is available
        if not template_details:
            self.log("Template {0} not found in project {1}".format(templateName, projectName))
            self.msg = "Template : {0} missing, new template to be created".format(templateName)
            self.status = "success"
            return self

        config["templateId"] = template_details.get("id")
        have_template["id"] = template_details.get("id")
        # Get available templates which are committed under the project
        template_list = self.dnac_apply['exec'](
            family="configuration_templates",
            function="gets_the_templates_available",
            params={"projectNames": config.get("projectName")},
        )
        have_template["isCommitPending"] = True
        # This check will fail if specified template is there not committed in dnac
        if template_list and isinstance(template_list, list):
            template_info = get_dict_result(template_list,
                                            "name",
                                            templateName)
            if template_info:
                template = self.get_template(config)
                have_template["template"] = template
                have_template["isCommitPending"] = False
                have_template["template_found"] = template is not None \
                    and isinstance(template, dict)
                self.log("Template {0} is found and template "
                         "details are :{1}".format(templateName, str(template)))

        # There are committed templates in the project but the
        # one specified in the playbook may not be committed
        self.log("Commit pending for template name {0}"
                 " is {1}".format(templateName, have_template.get('isCommitPending')))

        self.have_template = have_template
        self.msg = "Successfully collected all template parameters from dnac for comparison"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current project and template details from DNAC.

        Parameters:
            config (dict) - Playbook details containing Project/Template information.

        Returns:
            self
        """
        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            if not configuration_templates.get("project_name"):
                self.msg = "Mandatory Parameter project_name not available"
                self.status = "failed"
                return self
            template_available = self.get_have_project(config)
            if template_available:
                self.get_have_template(config, template_available)

        self.msg = "Successfully collected all project and template \
                    parameters from dnac for comparison"
        self.status = "success"
        return self

    def get_project_details(self, projectName):
        """
        Get the details of specific project name provided.

        Parameters:
            projectName (str) - Project Name

        Returns:
            items (dict) - Project details with given project name.
        """

        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function='get_projects',
            op_modifies=True,
            params={"name": projectName},
        )
        return items

    def get_want(self, config):
        """
        Get all the template and project related information from playbook
        that is needed to be created in DNAC.

        Parameters:
            config (dict) - Playbook details.

        Returns:
            self
        """

        want = {}
        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            template_params = self.get_template_params(config)
            project_params = self.get_project_params(config)
            version_comments = configuration_templates.get("version_description")

            if self.params.get("state") == "merged":
                self.update_mandatory_parameters(template_params)

            want["template_params"] = template_params
            want["project_params"] = project_params
            want["comments"] = version_comments

        self.want = want
        self.msg = "Successfully collected all parameters from playbook " + \
                   "for comparison"
        self.status = "success"
        return self

    def create_project_or_template(self, is_create_project=False):
        """
        Call DNAC API to create project or template based on the input provided.

        Parameters:
            is_create_project (bool) - Default value is False.

        Returns:
            creation_id (str) - Project Id.
            created (str) - True if Project created, else False.
        """

        creation_id = None
        created = False
        self.log(str(self.want))
        template_params = self.want.get("template_params")
        project_params = self.want.get("project_params")

        if is_create_project:
            self.log("entered")
            params_key = project_params
            name = "project: {0}".format(project_params.get('name'))
            validation_string = "Successfully created project"
            creation_value = "create_project"
        else:
            params_key = template_params
            name = "template: {0}".format(template_params.get('name'))
            validation_string = "Successfully created template"
            creation_value = "create_template"

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=creation_value,
            op_modifies=True,
            params=params_key,
        )
        if not isinstance(response, dict):
            self.log("Response not in dictionary format.")
            return creation_id, created

        task_id = response.get("response").get("taskId")
        if not task_id:
            self.log("Task id {0} not found".format(task_id))
            return creation_id, created

        while not created:
            task_details = self.get_task_details(task_id)
            if not task_details:
                self.log("Failed to get task details for taskid: {0}".format(task_id))
                return creation_id, created

            self.log("task_details: {0}".format(task_details))
            if task_details.get("isError"):
                self.log("isError set to true for taskid: {0}".format(task_id))
                return creation_id, created

            if validation_string not in task_details.get("progress"):
                self.log("progress set to {0} "
                         "for taskid: {1}".format(task_details.get('progress'), task_id))
                continue

            creation_id = task_details.get("data")
            if not creation_id:
                self.log("data is not found for taskid: {0}".format(task_id))
                continue

            created = True
            if is_create_project:
                # ProjectId is required for creating a new template.
                # Store it with other template parameters.
                template_params["projectId"] = creation_id
                template_params["project_id"] = creation_id

        self.log("New {0} created with id {1}".format(name, creation_id))
        return creation_id, created

    def requires_update(self):
        """
        Check if the template config given requires update.

        Parameters:
            self - Current object.

        Returns:
            bool - True if any parameter specified in obj_params differs between
            current_obj and requested_obj, indicating that an update is required.
            False if all specified parameters are equal.
        """

        if self.have_template.get("isCommitPending"):
            self.log("Template is in saved state and needs to be updated and committed")
            return True

        current_obj = self.have_template.get("template")
        requested_obj = self.want.get("template_params")
        obj_params = [
            ("tags", "tags", ""),
            ("author", "author", ""),
            ("composite", "composite", False),
            ("containingTemplates", "containingTemplates", []),
            ("createTime", "createTime", ""),
            ("customParamsOrder", "customParamsOrder", False),
            ("description", "description", ""),
            ("deviceTypes", "deviceTypes", []),
            ("failurePolicy", "failurePolicy", ""),
            ("id", "id", ""),
            ("language", "language", "VELOCITY"),
            ("lastUpdateTime", "lastUpdateTime", ""),
            ("latestVersionTime", "latestVersionTime", ""),
            ("name", "name", ""),
            ("parentTemplateId", "parentTemplateId", ""),
            ("projectId", "projectId", ""),
            ("projectName", "projectName", ""),
            ("rollbackTemplateContent", "rollbackTemplateContent", ""),
            ("rollbackTemplateParams", "rollbackTemplateParams", []),
            ("softwareType", "softwareType", ""),
            ("softwareVariant", "softwareVariant", ""),
            ("softwareVersion", "softwareVersion", ""),
            ("templateContent", "templateContent", ""),
            ("templateParams", "templateParams", []),
            ("validationErrors", "validationErrors", {}),
            ("version", "version", ""),
        ]

        return any(not dnac_compare_equality(current_obj.get(dnac_param, default),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param, default) in obj_params)

    def update_mandatory_parameters(self, template_params):
        """
        Update parameters which are mandatory for creating a template.

        Parameters:
            template_params (dict) - Template information.

        Returns:
            None
        """

        # Mandate fields required for creating a new template.
        # Store it with other template parameters.
        template_params["projectId"] = self.have_project.get("id")
        template_params["project_id"] = self.have_project.get("id")
        # Update language,deviceTypes and softwareType if not provided for existing template.
        if not template_params.get("language"):
            template_params["language"] = self.have_template.get('template') \
                .get('language')
        if not template_params.get("deviceTypes"):
            template_params["deviceTypes"] = self.have_template.get('template') \
                .get('deviceTypes')
        if not template_params.get("softwareType"):
            template_params["softwareType"] = self.have_template.get('template') \
                .get('softwareType')

    def validate_input_merge(self, template_exists):
        """
        Validate input after getting all the parameters from DNAC.
        "If mandate like deviceTypes, softwareType and language "
        "already present in DNAC for a template."
        "It is not required to be provided in playbook, "
        "but if it is new creation error will be thrown to provide these fields.

        Parameters:
            template_exists (bool) - True if template exists, else False.

        Returns:
            None
        """

        template_params = self.want.get("template_params")
        language = template_params.get("language").upper()
        if language:
            if language not in self.accepted_languages:
                self.msg = "Invalid value language {0} ." \
                           "Accepted language values are {1}" \
                           .format(self.accepted_languages, language)
                self.status = "failed"
                return self
        else:
            template_params["language"] = "JINJA"

        if not template_exists:
            if not template_params.get("deviceTypes") \
               or not template_params.get("softwareType"):
                self.msg = "DeviceTypes and SoftwareType are required arguments to create Templates"
                self.status = "failed"
                return self

        self.msg = "Input validated for merging"
        self.status = "success"
        return self

    def get_export_template_values(self, export_values):
        """
        Get the export template values from the details provided by the playbook.

        Parameters:
            export_values (bool) - All the template available under the project.

        Returns:
            self
        """

        template_details = self.dnac._exec(
            family="configuration_templates",
            function='get_projects_details'
        )
        for values in export_values:
            self.log(str(values.get("projectName")))
            template_details = template_details.get("response")
            all_template_details = get_dict_result(template_details,
                                                   "name",
                                                   values.get("projectName"))
            self.log(str(all_template_details))
            all_template_details = all_template_details.get("templates")
            self.log(str(all_template_details))
            template_detail = get_dict_result(all_template_details,
                                              "name",
                                              values.get("templateName"))
            self.log(str(template_detail))
            if template_detail is None:
                self.msg = "Invalid project_name and template_name in export"
                self.status = "failed"
                return self
            self.export_template.append(template_detail.get("id"))

        self.msg = "Successfully collected the export template IDs"
        self.status = "success"
        return self

    def export_project_or_tempalte(self, export):
        """
        Export templates and projects in DNAC with fields provided in DNAC.

        Parameters:
            export (dict) - Playbook details containing export information.

        Returns:
            None
        """

        export_project = export.get("project")
        self.log(str(export_project))
        if export_project:
            response = self.dnac._exec(
                family="configuration_templates",
                function='export_projects',
                params={"payload": export_project},
            )
            validation_string = "successfully exported project"
            self.check_task_response_status(response, validation_string, True).check_return_status()
            self.result['response'][0].update({"exportProject": self.msg})

        export_values = export.get("template")
        if export_values:
            self.get_export_template_values(export_values).check_return_status()
            self.log(str(self.export_template))
            response = self.dnac._exec(
                family="configuration_templates",
                function='export_templates',
                params={"payload": self.export_template},
            )
            validation_string = "successfully exported template"
            self.check_task_response_status(response, validation_string, True).check_return_status()
            self.result['response'][0].update({"exportTemplate": self.msg})

    def import_project_or_template(self, _import):
        """
        Import templates and projects in DNAC with fields provided in DNAC.

        Parameters:
            _import (dict) - Playbook details containing import information.

        Returns:
            None
        """

        do_version = _import.get("project").get("do_version")
        payload = None
        if _import.get("project").get("payload"):
            payload = _import.get("project").get("payload")
        else:
            self.msg = "Mandatory parameter payload is not found under import project"
            self.status = "failed"
            return self
        _import_project = {
            "do_version": do_version,
            # "payload": "{0}".format(payload)
            "payload": payload
        }
        self.log(str(_import_project))
        if _import_project:
            response = self.dnac._exec(
                family="configuration_templates",
                function='imports_the_projects_provided',
                params=_import_project,
            )
            validation_string = "successfully imported project"
            self.check_task_response_status(response, validation_string).check_return_status()
            self.result['response'][0].update({"importProject": validation_string})

        _import_template = _import.get("template")
        if _import_template:
            self.msg = "Mandatory paramter template is not found"
            self.status = "failed"
            return self
        if _import_template.get("projectName"):
            self.msg = "Mandatory paramter project_name is not found under import template"
            self.status = "failed"
            return self
        if _import_template.get("payload"):
            self.msg = "Mandatory paramter payload is not found under import template"
            self.status = "failed"
            return self

        self.log(str(_import_template))
        if _import_template:
            response = self.dnac._exec(
                family="configuration_templates",
                function='imports_the_templates_provided',
                params=_import_template,
            )
            validation_string = "successfully imported template"
            self.check_task_response_status(response, validation_string).check_return_status()
            self.result['response'][0].update({"importTemplate": validation_string})

    def get_diff_merged(self, config):
        """
        Update/Create templates and projects in DNAC with fields provided in DNAC.

        Parameters:
            config (dict) - Playbook details containing template information.

        Returns:
            self
        """

        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            is_project_found = self.have_project.get("project_found")
            if not is_project_found:
                project_id, project_created = \
                    self.create_project_or_template(is_create_project=True)
                if project_created:
                    self.log("project created with projectId : {0}".format(project_id))
                else:
                    self.status = "failed"
                    self.msg = "Project creation failed"
                    return self

            is_template_found = self.have_template.get("template_found")
            template_params = self.want.get("template_params")
            template_id = None
            template_updated = False
            self.validate_input_merge(is_template_found).check_return_status()
            if is_template_found:
                if self.requires_update():
                    response = self.dnac_apply['exec'](
                        family="configuration_templates",
                        function="update_template",
                        params=template_params,
                        op_modifies=True,
                    )
                    template_updated = True
                    template_id = self.have_template.get("id")
                    self.log("Updating Existing Template")
                else:
                    # Template does not need update
                    self.result['response'] = self.have_template.get("template")
                    self.result['msg'] = "Template does not need update"
                    self.status = "exited"
                    return self
            else:
                if template_params.get("name"):
                    template_id, template_updated = self.create_project_or_template()
                else:
                    self.msg = "missing required arguments: template_name"
                    self.status = "failed"
                    return self

            if template_updated:
                # Template needs to be versioned
                version_params = {
                    "comments": self.want.get("comments"),
                    "templateId": template_id
                }
                response = self.dnac_apply['exec'](
                    family="configuration_templates",
                    function="version_template",
                    op_modifies=True,
                    params=version_params
                )
                task_details = {}
                task_id = response.get("response").get("taskId")
                if not task_id:
                    self.msg = "Task id: {0} not found".format(task_id)
                    self.status = "failed"
                    return self
                task_details = self.get_task_details(task_id)
                self.result['changed'] = True
                self.result['msg'] = task_details.get('progress')
                self.result['diff'] = config.get("configuration_templates")
                self.log(str(task_details))
                self.result['response'] = task_details if task_details else response

                if not self.result.get('msg'):
                    self.msg = "Error while versioning the template"
                    self.status = "failed"
                    return self

        export = config.get("export")
        if export:
            self.export_project_or_tempalte(export)

        _import = config.get("import")
        if _import:
            # _import_project = _import.get("project")
            self.import_project_or_template(_import)

        self.msg = "Successfully completed merged state execution"
        self.status = "success"
        return self

    def delete_project_or_template(self, config, is_delete_project=False):
        """
        Call DNAC API to delete project or template with provided inputs.

        Parameters:
            config (dict) - Playbook details containing template information.
            is_delete_project (bool) - True if we need to delete project, else False.

        Returns:
            self
        """

        if is_delete_project:
            params_key = {"project_id": self.have_project.get("id")}
            deletion_value = "deletes_the_project"
            name = "project: {0}".format(config.get("configuration_templates").get('project_name'))
        else:
            template_params = self.want.get("template_params")
            params_key = {"template_id": self.have_template.get("id")}
            deletion_value = "deletes_the_template"
            name = "templateName: {0}".format(template_params.get('templateName'))

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=deletion_value,
            params=params_key,
        )
        task_id = response.get("response").get("taskId")
        if task_id:
            task_details = self.get_task_details(task_id)
            self.result['changed'] = True
            self.result['msg'] = task_details.get('progress')
            self.result['diff'] = config.get("configuration_templates")

            self.log(str(task_details))
            self.result['response'] = task_details if task_details else response
            if not self.result['msg']:
                self.result['msg'] = "Error while deleting {name} : "
                self.status = "failed"
                return self

        self.msg = "Successfully deleted {0} ".format(name)
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete projects or templates in DNAC with fields provided in playbook.

        Parameters:
            config (dict) - Playbook details containing template information.

        Returns:
            self
        """

        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            is_project_found = self.have_project.get("project_found")
            projectName = config.get("configuration_templates").get("project_name")

            if not is_project_found:
                self.msg = "Project {0} is not found".format(projectName)
                self.status = "failed"
                return self

            is_template_found = self.have_template.get("template_found")
            template_params = self.want.get("template_params")
            templateName = config.get("configuration_templates").get("template_name")
            if template_params.get("name"):
                if is_template_found:
                    self.delete_project_or_template(config)
                else:
                    self.msg = "Invalid template {0} under project".format(templateName)
                    self.status = "failed"
                    return self
            else:
                self.log("Template Name is empty, deleting the project and associated templates")
                is_project_deletable = self.have_project.get("isDeletable")
                if is_project_deletable:
                    self.delete_project_or_template(config, is_delete_project=True)
                else:
                    self.msg = "Project is not deletable"
                    self.status = "failed"
                    return self

        self.msg = "Successfully completed delete state execution"
        self.status = "success"
        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values.

        Parameters:
            self - The current object.

        Returns:
            None
        """

        self.have_project.clear()
        self.have_template.clear()
        self.want.clear()


def main():
    """ main entry point for module execution"""

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    dnac_template = DnacTemplate(module)
    dnac_template.validate_input().check_return_status()
    state = dnac_template.params.get("state")
    if state not in dnac_template.supported_states:
        dnac_template.status = "invalid"
        dnac_template.msg = "State {0} is invalid".format(state)
        dnac_template.check_return_status()

    for config in dnac_template.validated_config:
        dnac_template.reset_values()
        dnac_template.get_have(config).check_return_status()
        dnac_template.get_want(config).check_return_status()
        dnac_template.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_template.result)


if __name__ == '__main__':
    main()
