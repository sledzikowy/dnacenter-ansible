terraform {
  required_providers {
    esxi = {
      source = "registry.terraform.io/josenk/esxi"
      #
      # For more information, see the provider source documentation:
      # https://github.com/josenk/terraform-provider-esxi
      # https://registry.terraform.io/providers/josenk/esxi
    }
  }
}

variable vsphere_server {}
variable vsphere_host {}
variable vsphere_password {}
variable vsphere_user {}
variable env_prefix {}

provider "vsphere" {
  user                 = var.vsphere_user
  password             = var.vsphere_password
  vsphere_server       = var.vsphere_server
  allow_unverified_ssl = true
}

data "vsphere_datacenter" "datacenter" {
  name = "SOL-AUTO"
}

data "vsphere_host" "host" {
  name          = var.vsphere_host
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# VMS

data "vsphere_datastore" "datastore" {
    name = "datastore1"
    datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_resource_pool" "resource_pool" {
    name = "${var.vsphere_host}/Resources/"
    datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "vm-network" {
  name          = "VM Network"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "fusion-dnac-network" {
  name          = "Fusion_DNAC"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "fusion-ny-border" {
  name          = "Fusion_ny_Border"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "fusion-sj-border" {
  name          = "Fusion_sj_Border"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "fusion-sj-wlc" {
  name          = "Fusion_sj_wlc"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "fusion-ny-ewlc" {
  name          = "Fusion_ny_ewlc"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

resource "vsphere_file" "dnac-config-upload" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "dnac-config-cdrom.iso"
  destination_file   = "isos/dnac_config-cdrom.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "dnac-test" {
    depends_on = [vsphere_file.dnac-config-upload]
    count = 1
    name = "dnac-test"
    num_cpus = 32
    cpu_reservation = 64000
    memory = 262144
    memory_reservation = 262144
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

  network_interface {
    network_id = data.vsphere_network.fusion-dnac-network.id
    ovf_mapping = "Network 1"
  }
  network_interface {
    network_id = data.vsphere_network.vm-network.id
    ovf_mapping = "Network 2"
  }
    
    cdrom {
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/dnac_config-cdrom.iso"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/assembly_release_dnac_hulk-patch4_converged_07-3.718.75330.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_file" "cat9k-iso" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.iso"
  destination_file   = "isos/cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.iso"
  create_directories = true
}

resource "vsphere_file" "ny-border-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "ny_border_config.iso"
  destination_file   = "isos/ny_border_config.iso"
  create_directories = true
}


resource "vsphere_virtual_machine" "ny-border-test" {
    depends_on = [vsphere_file.cat9k-iso, vsphere_file.ny-border-config]
    count = 1
    name = "ny-border-test"
    num_cpus = 8
    memory = 32768
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

  network_interface {
    network_id = data.vsphere_network.fusion-ny-border.id
    ovf_mapping = "Network 3"
  }
  network_interface {
    network_id = data.vsphere_network.vm-network.id
    ovf_mapping = "Network 2"
  }

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.iso"
    }

    cdrom {
      # client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/ny_border_config.iso"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_file" "sj-border-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "sj_border_config.iso"
  destination_file   = "isos/sj_border_config.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "sj-border-test" {
    depends_on = [vsphere_file.cat9k-iso, vsphere_file.sj-border-config]
    count = 1
    name = "sj-border-test"
    num_cpus = 8
    memory = 32768
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.iso"
    }

    cdrom {
      client_device = true
      #datastore_id = data.vsphere_datastore.datastore.id
      #path         = "isos/sj_border_config.iso"
    }

  network_interface {
    network_id = data.vsphere_network.fusion-sj-border.id
    ovf_mapping = "Network 3"
  }
  network_interface {
    network_id = data.vsphere_network.vm-network.id
    ovf_mapping = "Network 2"
  }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/cat9kv-universalk9_serial.BLD_V1715_THROTTLE_LATEST_20240612_002610.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_file" "c8000-iso" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "c8000v-universalk9_vga.17.14.01a.iso"
  destination_file   = "isos/c8000v-universalk9_vga.17.14.01a.iso"
  create_directories = true
}

resource "vsphere_file" "transit-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "transit_config.iso"
  destination_file   = "isos/transit_config.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "transit-test" {
    depends_on = [ vsphere_file.transit-config, vsphere_file.c8000-iso ]
    count = 1
    name = "transit-test"
    num_cpus = 4
    memory = 16384
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/c8000v-universalk9_vga.17.14.01a.iso"
    }

    cdrom {
      client_device = true
      #datastore_id = data.vsphere_datastore.datastore.id
      #path         = "isos/transit_config.iso"
    }

    network_interface {
      network_id = data.vsphere_network.vm-network.id
      ovf_mapping = "Network 2"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/c8000v-universalk9.17.14.01a.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_file" "fusion-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "fusion_config.iso"
  destination_file   = "isos/fusion_config.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "fusion-switch-test" {
    depends_on = [ vsphere_file.c8000-iso, vsphere_file.fusion-config ]
    count = 1
    name = "fusion-switch-test"
    num_cpus = 4
    memory = 32768
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/c8000v-universalk9_vga.17.14.01a.iso"
    }

    cdrom {
#      client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/fusion_config.iso"
    }

    network_interface {
      network_id = data.vsphere_network.vm-network.id
      ovf_mapping = "Network 2"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-ny-border.id
      ovf_mapping = "Network 3"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-sj-border.id
      ovf_mapping = "Network 4"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-sj-wlc.id
      ovf_mapping = "Network 5"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-ny-ewlc.id
      ovf_mapping = "Network 6"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-dnac-network.id
      ovf_mapping = "Network 7"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/c8000v-universalk9.17.14.01a.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_virtual_machine" "ise-test" {
    count = 1
    name = "ise-test"
    num_cpus = 24
    memory = 32768
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    network_interface {
      network_id = data.vsphere_network.vm-network.id
      ovf_mapping = "Network 2"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-dnac-network.id
      ovf_mapping = "Network 3"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/ISE-3.2.0.542b-virtual-SNS3715-SNS3755-300.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
    vapp {
      properties = {
        user-data = base64encode(templatefile("user_data.tftpl", {
          hostname          = "ISE"
          primarynameserver = ""
          dnsdomain         = ""
          ntpserver         = ""
          timezone          = ""
          password          = "LabLab123!"
          ersapi            = ""
          openapi           = ""
          pxGrid            = ""
          pxgrid_cloud      = ""
        }))
      }
    }
}


resource "vsphere_file" "vwlc-iso" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "AS_CTVM_SMALL_8_10_196_0.iso"
  destination_file   = "isos/AS_CTVM_SMALL_8_10_196_0.iso"
  create_directories = true
}

resource "vsphere_file" "sj-wlc-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "sj_wlc_config.iso"
  destination_file   = "isos/sj_wlc_config.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "sj-wlc-test" {
    depends_on = [ vsphere_file.vwlc-iso, vsphere_file.sj-wlc-config ]
    count = 1
    name = "sj-wlc-test"
    num_cpus = 6
    memory = 16392
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/AS_CTVM_SMALL_8_10_196_0.iso"
    }

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/sj_wlc_config.iso"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-sj-wlc.id
      ovf_mapping = "VM Network"
    }

    network_interface {
      network_id = data.vsphere_network.vm-network.id
      ovf_mapping = "VM Network 2"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/AIR_CTVM-K9_8_10_196_0.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}

resource "vsphere_file" "ny-wlc-config" {
  datacenter         = data.vsphere_datacenter.datacenter.name
  datastore          = data.vsphere_datastore.datastore.name
  source_file        = "ny_wlc_config.iso"
  destination_file   = "isos/ny_wlc_config.iso"
  create_directories = true
}

resource "vsphere_virtual_machine" "ny-wlc-test" {
    count = 1
    name = "ny-wlc-test"
    num_cpus = 6
    memory = 16392
    resource_pool_id = data.vsphere_resource_pool.resource_pool.id
    datastore_id = data.vsphere_datastore.datastore.id
    host_system_id = data.vsphere_host.host.id
    datacenter_id = data.vsphere_datacenter.datacenter.id

    wait_for_guest_net_routable = false
    wait_for_guest_net_timeout = 0
    wait_for_guest_ip_timeout  = 0

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/AS_CTVM_SMALL_8_10_196_0.iso"
    }

    cdrom {
      #client_device = true
      datastore_id = data.vsphere_datastore.datastore.id
      path         = "isos/ny_wlc_config.iso"
    }

    network_interface {
      network_id = data.vsphere_network.fusion-ny-ewlc.id
      ovf_mapping = "VM Network"
    }

    network_interface {
      network_id = data.vsphere_network.vm-network.id
      ovf_mapping = "VM Network 2"
    }

    ovf_deploy {
      allow_unverified_ssl_cert = true
      #remote_ovf_url            = "http://10.195.243.37/noble-server-cloudimg-amd64.ova"
      local_ovf_path = "/home/cisco/topo/AIR_CTVM-K9_8_10_196_0.ova"
      disk_provisioning         = "thin"
      ip_protocol               = "IPV4"
      ip_allocation_policy      = "STATIC_MANUAL"
    }
}
