# Changelog

## 0.11.0 (2026-04-30)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.10.0...v0.11.0)

### Features

* support setting headers via env ([b37d612](https://github.com/linkt-ai/linkt-python-sdk/commit/b37d61229d235fa453e7f960d70f5d41d324f565))


### Bug Fixes

* use correct field name format for multipart file arrays ([6ca9fb9](https://github.com/linkt-ai/linkt-python-sdk/commit/6ca9fb9f3448765854b82c71815ed0929ec72ffb))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([9f3490f](https://github.com/linkt-ai/linkt-python-sdk/commit/9f3490ff373baa01a0b9616809d716c6fd2e2e6b))


### Chores

* **internal:** more robust bootstrap script ([a6df833](https://github.com/linkt-ai/linkt-python-sdk/commit/a6df833f8d059242b91db934864375319c70d36c))

## 0.10.0 (2026-04-14)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([e386e9a](https://github.com/linkt-ai/linkt-python-sdk/commit/e386e9a69c09f39e45da40ebb5bf970f2221f095))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([e2e956c](https://github.com/linkt-ai/linkt-python-sdk/commit/e2e956c881eaf4be7b2d8bd42833a27e1da1f77b))
* ensure file data are only sent as 1 parameter ([bf842ad](https://github.com/linkt-ai/linkt-python-sdk/commit/bf842ad2d05c8c604a45e8b8eea845c04c518c37))

## 0.9.0 (2026-04-01)

Full Changelog: [v0.8.1...v0.9.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.8.1...v0.9.0)

### Features

* **internal:** implement indices array format for query and form serialization ([8f1bc15](https://github.com/linkt-ai/linkt-python-sdk/commit/8f1bc155afda31ea02c5245836f8b6578202ba7e))


### Chores

* **ci:** skip lint on metadata-only changes ([27d3f59](https://github.com/linkt-ai/linkt-python-sdk/commit/27d3f59b6fc7699216b74d8ba6596f3ac18a5f13))
* **internal:** update gitignore ([22b6fae](https://github.com/linkt-ai/linkt-python-sdk/commit/22b6faebdd77a146bbcc098a9c7cfc29f5efda66))

## 0.8.1 (2026-03-20)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.8.0...v0.8.1)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([8396aea](https://github.com/linkt-ai/linkt-python-sdk/commit/8396aea4a4d089295d404b7a1f82963476cf6c93))
* **pydantic:** do not pass `by_alias` unless set ([7064add](https://github.com/linkt-ai/linkt-python-sdk/commit/7064addba06aba678aeb777fab3be02338bdee0d))
* sanitize endpoint path params ([53ea547](https://github.com/linkt-ai/linkt-python-sdk/commit/53ea54762aad99ed038b545ecc07834092d673ff))


### Chores

* **internal:** tweak CI branches ([3d2e11f](https://github.com/linkt-ai/linkt-python-sdk/commit/3d2e11f552949c5c932eaa30a28d19cdc287c0e9))

## 0.8.0 (2026-03-08)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([d8f1aef](https://github.com/linkt-ai/linkt-python-sdk/commit/d8f1aefb117cdb1af4d396f9593272ccc0e98944))
* **api:** api update ([2bce784](https://github.com/linkt-ai/linkt-python-sdk/commit/2bce784d58a8876f245e4c333774eb0c91a37f5e))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([a3596d9](https://github.com/linkt-ai/linkt-python-sdk/commit/a3596d93f7b8175f16f1d49a6cb80c335b11ce9e))

## 0.7.0 (2026-03-05)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([cfb7e36](https://github.com/linkt-ai/linkt-python-sdk/commit/cfb7e36b7e79c6dcd0a933462aa1180e507f80ad))
* **api:** api update ([56ce393](https://github.com/linkt-ai/linkt-python-sdk/commit/56ce3936f27ae4e6f5a071e819d1e4b7491054d8))
* **api:** api update ([65678d4](https://github.com/linkt-ai/linkt-python-sdk/commit/65678d45540cdec59d7d3cca77da1acab33b9674))
* **api:** api update ([a9ee53e](https://github.com/linkt-ai/linkt-python-sdk/commit/a9ee53e93224d5f793a6005d704aee4c4df59963))
* **api:** api update ([833dea4](https://github.com/linkt-ai/linkt-python-sdk/commit/833dea4a8b7a2d5fb7849a53560c88c2223ab52a))
* **api:** api update ([cb3eaa7](https://github.com/linkt-ai/linkt-python-sdk/commit/cb3eaa7ab3afecaefe2a588c1d6ba40c1b981edd))


### Chores

* **api:** minor updates ([63a3cbe](https://github.com/linkt-ai/linkt-python-sdk/commit/63a3cbe48ebf52ec02b810ea8a86b5c655c8a8be))
* **ci:** bump uv version ([00ba9dd](https://github.com/linkt-ai/linkt-python-sdk/commit/00ba9dd09e60c560c73e96cdc63c677a82b4c099))
* format all `api.md` files ([a511a92](https://github.com/linkt-ai/linkt-python-sdk/commit/a511a92ae5a08f0ca9428ee65588cad324ca1f4c))
* **internal:** add request options to SSE classes ([20c90cb](https://github.com/linkt-ai/linkt-python-sdk/commit/20c90cb6970c1d8189f7a8b320fbd1eb2d25df3e))
* **internal:** bump dependencies ([4d821cf](https://github.com/linkt-ai/linkt-python-sdk/commit/4d821cffadc156abd82a8d4dabe35d5ed8f96410))
* **internal:** codegen related update ([026d119](https://github.com/linkt-ai/linkt-python-sdk/commit/026d119742e7f640113fbfb4da03ce94c56f7f58))
* **internal:** fix lint error on Python 3.14 ([dfb23aa](https://github.com/linkt-ai/linkt-python-sdk/commit/dfb23aa8f1544e0248f4129e0e8396f2c26b35bb))
* **internal:** make `test_proxy_environment_variables` more resilient ([5174ea1](https://github.com/linkt-ai/linkt-python-sdk/commit/5174ea10feb9852bdc1390cf41ff70562bb43e24))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([feb1e12](https://github.com/linkt-ai/linkt-python-sdk/commit/feb1e12a0b9b49665367d0bb2b8af78b62e38e20))
* **internal:** remove mock server code ([2a0dc39](https://github.com/linkt-ai/linkt-python-sdk/commit/2a0dc39733f4e47ba1494d3c22cd3db2dd1a93b4))
* update mock server docs ([fb761bd](https://github.com/linkt-ai/linkt-python-sdk/commit/fb761bdec53e0ba486fafe6d10cfa3a039099a66))

## 0.6.0 (2026-02-05)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([2ec3ca1](https://github.com/linkt-ai/linkt-python-sdk/commit/2ec3ca1d5612c71532e555544c91175d0eda59f3))
* **api:** api update ([869a502](https://github.com/linkt-ai/linkt-python-sdk/commit/869a5021ea9ece9b3e7fe1caed65fda03dc81d85))
* **client:** add custom JSON encoder for extended type support ([a5ff81d](https://github.com/linkt-ai/linkt-python-sdk/commit/a5ff81d8764a933a98a8bc7dc0bb151fe2eab2a5))

## 0.5.0 (2026-01-27)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([ada2d6b](https://github.com/linkt-ai/linkt-python-sdk/commit/ada2d6bfac570f2e150d357d84b0c50e4a915908))
* **api:** api update ([1f4a701](https://github.com/linkt-ai/linkt-python-sdk/commit/1f4a7016a2daba5cb49d1cead52065b8e5511ec5))
* **api:** api update ([47addbc](https://github.com/linkt-ai/linkt-python-sdk/commit/47addbc0539accf083a9322b0ca60f8b1eb05b07))


### Chores

* **ci:** upgrade `actions/github-script` ([a65d1c0](https://github.com/linkt-ai/linkt-python-sdk/commit/a65d1c0e13a0e1ad1896bc433dd13590cfd07e21))

## 0.4.0 (2026-01-22)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([62abd11](https://github.com/linkt-ai/linkt-python-sdk/commit/62abd116eeb33f1cfbed7f168b7ff1dbf9692ada))
* **api:** api update ([bcf385a](https://github.com/linkt-ai/linkt-python-sdk/commit/bcf385acb484fbdb0433ef169f28c566577d9d5e))
* **api:** api update ([661e5df](https://github.com/linkt-ai/linkt-python-sdk/commit/661e5df21b88701dcda66f9938eae433f4205e5a))
* **api:** clear entity model ([04de84b](https://github.com/linkt-ai/linkt-python-sdk/commit/04de84b8fc139b98c65fcf1d099f3cd115cf11bc))
* **api:** manual update ([f2276cd](https://github.com/linkt-ai/linkt-python-sdk/commit/f2276cd9fad98f973d9b380718cc778dfdadc08d))
* **client:** add support for binary request streaming ([6a566cc](https://github.com/linkt-ai/linkt-python-sdk/commit/6a566cc8d61d3a263f20429041548d0b4335ad29))


### Chores

* **internal:** update `actions/checkout` version ([a060ed3](https://github.com/linkt-ai/linkt-python-sdk/commit/a060ed32a132835b44884a22ffb1f0680e2ddeb9))

## 0.3.0 (2026-01-09)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([79a8673](https://github.com/linkt-ai/linkt-python-sdk/commit/79a8673aebcc7ce5a01e0b2e82001daf1d775632))
* **api:** api update ([ecf9563](https://github.com/linkt-ai/linkt-python-sdk/commit/ecf9563fed6dcb1a99bd0e5b84b2d5f7bc677b58))


### Chores

* update yaml config task model reference ([1d8f3c1](https://github.com/linkt-ai/linkt-python-sdk/commit/1d8f3c147e781163cf47b9b91ed51b20b329461a))

## 0.2.0 (2026-01-08)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.1.0...v0.2.0)

### Features

* enable pypi publishing ([129756c](https://github.com/linkt-ai/linkt-python-sdk/commit/129756c80710ea93368dff36f0baa13cc5d63c1a))
* set production as default environment ([ece50de](https://github.com/linkt-ai/linkt-python-sdk/commit/ece50defdc0579504f9f79d5dc3f178185eed789))
* update project name ([3bde99f](https://github.com/linkt-ai/linkt-python-sdk/commit/3bde99fe29c9b4ece62a29c1b74b352d08ddeca2))

## 0.1.0 (2026-01-08)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/linkt-ai/linkt-python-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([7a3996c](https://github.com/linkt-ai/linkt-python-sdk/commit/7a3996cc92b5b984210de602634bb6ba26c55a69))
* updates to environments ([555add7](https://github.com/linkt-ai/linkt-python-sdk/commit/555add776af48aaaec5061a8fa7266607657cd45))


### Chores

* update SDK settings ([5a376fd](https://github.com/linkt-ai/linkt-python-sdk/commit/5a376fdeba8b8e8d82bb70b47a2b991d3d6448ad))
