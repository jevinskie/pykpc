# type: ignore

from cffi import FFI

ffi = FFI()
ffi.cdef("""
#define KPC_PMU_ERROR 0
#define KPC_PMU_INTEL_V3 1
#define KPC_PMU_ARM_APPLE 2
#define KPC_PMU_INTEL_V2 3
#define KPC_PMU_ARM_V2 4
#define KPC_CLASS_FIXED 0
#define KPC_CLASS_CONFIGURABLE 1
#define KPC_CLASS_POWER 2
#define KPC_CLASS_RAWPMU 3
#define KPC_CLASS_FIXED_MASK 1u
#define KPC_CLASS_CONFIGURABLE_MASK 2u
#define KPC_CLASS_POWER_MASK 4u
#define KPC_CLASS_RAWPMU_MASK 8u
#define KPC_ALL_CPUS 0x80000000
typedef uint32_t kpc_classmask_t;
typedef uint64_t kpc_config_t;

int kpc_force_all_ctrs_set(int force);
int kpc_force_all_ctrs_get(int *forcing);
int kpc_get_thread_counters(int thread_id, uint32_t num_cntrs, uint64_t *cntrs);
uint32_t kpc_get_config_count(kpc_classmask_t classes);
uint32_t kpc_get_counter_count(kpc_classmask_t classes);
kpc_classmask_t kpc_get_thread_counting(void);
int kpc_set_thread_counting(kpc_classmask_t classes);
int kpc_cpu_string(char *buf, size_t size);
int kpc_pmu_version(void);

typedef uint32_t u_int;
int sysctl(int *name, u_int namelen, void *oldp, size_t *oldlenp, void *newp, size_t newlen);
int sysctlbyname(const char *name, void *oldp, size_t *oldlenp, void *newp, size_t newlen);
int sysctlnametomib(const char *name, int *mibp, size_t *sizep);
""")
C = ffi.dlopen("/System/Library/PrivateFrameworks/kperf.framework/kperf")
D = ffi.dlopen(None)

kver_node = ffi.new("char[]", b"kern.version")
print(f"kver_node: {kver_node}")
kver = ffi.new("char[1024]")
kver_sz = ffi.new("size_t*", 1024)
print(f"kver_sz: {kver_sz} {kver_sz[0]}")
kver_res = D.sysctlbyname(kver_node, kver, kver_sz, ffi.NULL, 0)
print(f"kver_res: {kver_res}")
print(f"kver_sz: {kver_sz} {kver_sz[0]}")
kver_str = ffi.string(kver)
print(f"kver: {kver} {kver_str} len: {len(kver_str)}")

pmu_ver = C.kpc_pmu_version()

print(f"pmu_ver: {pmu_ver}")

forcing_out_arg = ffi.new("int*", 3)

print(f"forcing_out 1: errno: {ffi.errno} {forcing_out_arg} {forcing_out_arg[0]}")

gr = C.kpc_force_all_ctrs_get(forcing_out_arg)

print(f"forcing_out 2: gr: {gr} errno: {ffi.errno} {forcing_out_arg} {forcing_out_arg[0]}")

sfr = C.kpc_force_all_ctrs_set(1)

print(f"set_forcing res: {sfr}")

gr2 = C.kpc_force_all_ctrs_get(forcing_out_arg)

print(f"forcing_out 3: gr: {gr2} errno: {ffi.errno} {forcing_out_arg} {forcing_out_arg[0]}")


# for i in range(258):
#     r = C.kpc_get_config_count(i)
#     print(f"i: {i:3} i: {i:#010b} r: {r:3} r: {r:#010b}")

cfg_cnt_fixed = C.kpc_get_config_count(C.KPC_CLASS_CONFIGURABLE_MASK)

print(f"KPC_CLASS_POWER: {C.KPC_CLASS_POWER} KPC_CLASS_POWER_MASK: {C.KPC_CLASS_POWER_MASK}")

print(f"cfg_cnt_fixed: {cfg_cnt_fixed}")
