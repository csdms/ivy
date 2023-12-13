# Changelog

All notable changes to CSDMS Ivy will be documented in this file.

Automatically add updates with:
```bash
git-changelog --in-place --output CHANGES.md
```

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [v2023.2](https://github.com/csdms/ivy/releases/tag/v2023.2) - 2023-12-13

<small>[Compare with v2023.1](https://github.com/csdms/ivy/compare/v2023.1...v2023.2)</small>

### Added

- Add changelog instructions ([da37453](https://github.com/csdms/ivy/commit/da374536f4030e3932e171bf948f4112b0a6fd20) by Mark Piper).
- Add changelog created with git-changelog ([388361f](https://github.com/csdms/ivy/commit/388361f91b8b2d393d06ed39d7b61be38c2e13c5) by Mark Piper).
- Add a package definition file for relative imports ([9bc8393](https://github.com/csdms/ivy/commit/9bc8393ea932976b058cbda7b32aac24a6afcd9c) by Mark Piper).
- Add tests for Diffusion class ([dd4cd41](https://github.com/csdms/ivy/commit/dd4cd41c317f1649a691e1b236ebbb51eb26daa8) by Mark Piper).
- Add tests for solver module ([f8450af](https://github.com/csdms/ivy/commit/f8450afb70de66b833eff2a103bb30820b0d6b63) by Mark Piper).
- Add a note on reference copying ([d69d070](https://github.com/csdms/ivy/commit/d69d0702b2547fb4fd04516c383af0d96b93da6b) by Mark Piper).
- Add clarifying text on terminology ([d9a3fbc](https://github.com/csdms/ivy/commit/d9a3fbcc29d8c890c22b13f1427b5bd7f02a68aa) by Mark Piper).
- add a welcome notebook for the landlab lessons ([7ab776c](https://github.com/csdms/ivy/commit/7ab776c10b28160ad65f8ea5417f7a58a6c7a40e) by mcflugen).
- add an opentopography key ([918a99e](https://github.com/csdms/ivy/commit/918a99ed6279b7ba3624241b427ecfcc117a2eb9) by mcflugen).
- add section on mapping data between grids ([575cfb3](https://github.com/csdms/ivy/commit/575cfb33c971e04ac2068db861e8bcdc3c312b22) by mcflugen).
- add isort config to pyproject.toml ([02c13a0](https://github.com/csdms/ivy/commit/02c13a00035e424f9b4634457d836606d7853319) by mcflugen).
- add new landlab lesson notebooks ([b09d0ff](https://github.com/csdms/ivy/commit/b09d0ff39afffa1b2a2110fe7dedda3a34fb7244) by mcflugen).
- add args to hook to change notebook kernels ([d151edc](https://github.com/csdms/ivy/commit/d151edca24366a819ec7c4b27e729cf7d7cff0db) by mcflugen).
- add heartfelt-hooks; update hook versions ([30df437](https://github.com/csdms/ivy/commit/30df437725ba846bf366d943ffbe798908f5dea4) by mcflugen).
- Add summary; spellcheck ([c189528](https://github.com/csdms/ivy/commit/c189528c681c2cd5a526bf295b4c29d7b128fe95) by Mark Piper).
- Add intro paragraph ([ed8482e](https://github.com/csdms/ivy/commit/ed8482ee7305e3f94a27de078fdbef004d387acf) by Mark Piper).
- Add simple example and update text for DEM data example ([55d537b](https://github.com/csdms/ivy/commit/55d537b3de4a94e9a269b2c2bff2c77f63facecd) by Mark Piper).
- Add a notebook that shows how to plot shapes ([b9d1106](https://github.com/csdms/ivy/commit/b9d11068a6b8eb796f8d6ef2d21dbea48ffd54c2) by Mark Piper).
- Add concepts and examples ([b45632d](https://github.com/csdms/ivy/commit/b45632df7e802fcc951742a33979bb118763e4b8) by Mark Piper).
- Add shape demonstration classes ([11dd9e8](https://github.com/csdms/ivy/commit/11dd9e8b9a500500b1833a2f8c68f1c4ae43bd19) by Mark Piper).
- Add Python script example ([221be8c](https://github.com/csdms/ivy/commit/221be8caf49fdd37e0013c80d2df85f8b725860b) by Mark Piper).

### Fixed

- fix toc levels ([16812fb](https://github.com/csdms/ivy/commit/16812fbb025223fb87d6e4303944801f34dc5bcd) by mcflugen).
- fix inconsistent heading levels ([99c69c5](https://github.com/csdms/ivy/commit/99c69c5bf26d95c6969d87c2635aa31d5f597cdd) by mcflugen).
- Fix dostring example output fails ([7b671eb](https://github.com/csdms/ivy/commit/7b671ebfad933fa82c8d544010f3b55170444601) by Mark Piper).
- Fix error with function name ([81e459b](https://github.com/csdms/ivy/commit/81e459b28ba4505b02baeffc6ff64b7869a80bc0) by Mark Piper).
- Fix typos and spelling errors ([4f2c10a](https://github.com/csdms/ivy/commit/4f2c10a0aa22385d07b27a8366de0e8f4f742e2f) by Mark Piper).

### Changed

- change solution notebook extension to .a.ipynb ([8e5c2be](https://github.com/csdms/ivy/commit/8e5c2be7d7c26980bcb243321bfd18d06bdcd997) by mcflugen).

### Removed

- Remove unused import ([e33826d](https://github.com/csdms/ivy/commit/e33826d41dc060dd8f869f8e6e9194ca02d17141) by Mark Piper).
- Remove extra parameter that causes Agg backend to fail ([c829191](https://github.com/csdms/ivy/commit/c8291916db0c556b424aa3692c240a1ac9c29333) by Mark Piper).
- Remove matplotlib version restriction ([06d7504](https://github.com/csdms/ivy/commit/06d75041584fe4b7d4ca39d621203978cb515d35) by Mark Piper).
- Remove lint ([0f396a7](https://github.com/csdms/ivy/commit/0f396a7db6bf665f6ee92f833e66c18025badba6) by Mark Piper).
- Remove unused imports ([fef801b](https://github.com/csdms/ivy/commit/fef801bdd537fd5cf985b330c99b78cfb4e335e9) by Mark Piper).


## [v2023.1](https://github.com/csdms/ivy/releases/tag/v2023.1) - 2023-05-15

<small>[Compare with v2023.0](https://github.com/csdms/ivy/compare/v2023.0...v2023.1)</small>

### Added

- Add function and class (OOP) examples to Python lesson (#108) ([1ba1e4c](https://github.com/csdms/ivy/commit/1ba1e4c215807e800ba71a79e136944ae536e222) by Mark Piper).

### Fixed

- Fix error in docstring example ([f20200c](https://github.com/csdms/ivy/commit/f20200c18401625e3cb18b6a52e1b2d80d54e446) by Mark Piper).
- Fix incorrect parameter name ([4d39af9](https://github.com/csdms/ivy/commit/4d39af936c48b7035dc5c78b24bc5e7dcafcaf41) by Mark Piper).

## [v2023.0](https://github.com/csdms/ivy/releases/tag/v2023.0) - 2023-03-14

<small>[Compare with v2022.0](https://github.com/csdms/ivy/compare/v2022.0...v2023.0)</small>

### Added

- Add section on issues to git lesson (#97) ([3464d7a](https://github.com/csdms/ivy/commit/3464d7a6dc6f7183c82af002bb78b34860bfbe44) by Mark Piper).
- Add git remotes diagram (#94) ([bd39cde](https://github.com/csdms/ivy/commit/bd39cde566a672461dcb68e62f6fdc65a8113910) by Mark Piper).
- add ellipses in the for loop of a hint cell ([d02da96](https://github.com/csdms/ivy/commit/d02da96577c5dd3d72db5f08f3ab8d5c8df66dc1) by mcflugen).
- add solution notebook for creating a component ([a5572d8](https://github.com/csdms/ivy/commit/a5572d8474da214d5154eb9aff135d6e35437e35) by mcflugen).
- add session to insert toc and hide solutions ([73e9cfc](https://github.com/csdms/ivy/commit/73e9cfcf6569b77f55b8db6e5756ecb63b59035d) by mcflugen).
- add more notebook QA hooks ([aa68c8c](https://github.com/csdms/ivy/commit/aa68c8c22060a9c99208ed61d9655e03f04037f6) by mcflugen).
- add a create-a-component landlab notebook ([88954b6](https://github.com/csdms/ivy/commit/88954b6ea31eb04d49d335d191ebe442f721fc3f) by mcflugen).
- add landlab solution notebooks ([b0d7aa3](https://github.com/csdms/ivy/commit/b0d7aa3e5076ecf64655fd07c40087f8642ef333) by mcflugen).
- add data file, install requirements for best-practices ([a328b49](https://github.com/csdms/ivy/commit/a328b4966cab8cb6f19b5d00ee03c900458eb96a) by mcflugen).
- add matplotlib to requirements ([dac5726](https://github.com/csdms/ivy/commit/dac572602f3a48f273a1be0a5e6f87f6a27c3c4b) by mcflugen).
- add pytest settings file ([6ec1bbe](https://github.com/csdms/ivy/commit/6ec1bbe21f9da6ac3f848497574f1fbb9a618b78) by mcflugen).
- add zSW3.asc data file for tidal flow calculator ([992c5f9](https://github.com/csdms/ivy/commit/992c5f9dd0c7c15fce3367ca52b1518c972dcb77) by mcflugen).
- add file-contents-sorter hook for requirements files ([459fab3](https://github.com/csdms/ivy/commit/459fab3877f28d757355243a64917e1e693b6b57) by mcflugen).
- add hook to find and clean dirty notebooks ([0de3a79](https://github.com/csdms/ivy/commit/0de3a798c557f3f0e5d9352e6bc0b80905cf9bae) by mcflugen).
- add a requirements file for the notebooks ([413a2e6](https://github.com/csdms/ivy/commit/413a2e6bbc824ebb6377f7b2daf5a8b27da3ea44) by mcflugen).
- add flake8 settings file ([2a578c6](https://github.com/csdms/ivy/commit/2a578c610a3383bfa935ec87cda7fc6261fe4f61) by mcflugen).
- add pre-commit hooks for linting ([a73b01f](https://github.com/csdms/ivy/commit/a73b01fc43f966bc31e20ea3aa2886cac533f3ee) by mcflugen).
- Add link to BSSw blog post on git ([6ddf325](https://github.com/csdms/ivy/commit/6ddf32524ff8de857c45d88f759514b9ff9ac80b) by Mark Piper).
- Add code and toggle solution visibility in Landlab grids notebook (#87) ([a2d9e0b](https://github.com/csdms/ivy/commit/a2d9e0ba1b654fbfee2f7b9fe37491fffbb62d92) by Mark Piper).

### Removed

- remove old fault-scarp notebook from notebook list ([cc69b19](https://github.com/csdms/ivy/commit/cc69b195cea7a9998aa8a906f016c85fc89bf12b) by mcflugen).
- remove duplicate fault-scarp notebook ([bb9f119](https://github.com/csdms/ivy/commit/bb9f1199f1c9e14f82aa565d269e83580a14ec6c) by mcflugen).
- remove lint ([e4ba22d](https://github.com/csdms/ivy/commit/e4ba22da3f473cf628db958b3acfc5237e962a8c) by mcflugen).
- remove more notebook lint ([e9c8ef5](https://github.com/csdms/ivy/commit/e9c8ef55385a27df6ca58eeac88328a66ae6974f) by mcflugen).
- remove more lint ([3dc4c70](https://github.com/csdms/ivy/commit/3dc4c70e42f5daa9a313fcf3c6a201a797a82d28) by mcflugen).
- remove notebook lint ([6197062](https://github.com/csdms/ivy/commit/6197062d3ef1249b179d8cdde06af6b8eef1ec23) by mcflugen).
- remove unused data files ([a3b3d5f](https://github.com/csdms/ivy/commit/a3b3d5fcac10ba013ad88495a554b1f0c329ec88) by mcflugen).
- Remove notebook tutorial (#91) ([d9b1211](https://github.com/csdms/ivy/commit/d9b12111d12f129e7ba1c4f05977d23952c2d981) by Mark Piper).
- remove python 3.9 requirement for notebook tests ([4b1cdc2](https://github.com/csdms/ivy/commit/4b1cdc2d654bfabaf775d41ef46ea60e741ce295) by mcflugen).
- remove default sessions to run ([409ee5a](https://github.com/csdms/ivy/commit/409ee5a8b635f39ad821c90da949da75e541b238) by mcflugen).

## [v2022.0](https://github.com/csdms/ivy/releases/tag/v2022.0) - 2022-07-27

<small>[Compare with v1.1.1](https://github.com/csdms/ivy/compare/v1.1.1...v2022.0)</small>

### Added

- Add reference to Wilson et al. 2014 ([862fc8b](https://github.com/csdms/ivy/commit/862fc8bafa665864ceae25c4ead9e376ffe175cb) by Mark Piper).
- Add diffusion solution notebook ([a2bf2e0](https://github.com/csdms/ivy/commit/a2bf2e0767eeda767860133c6fd6697e38b3bdbb) by Benjamin Campforts).
- Add hylands notebook ([f90c87c](https://github.com/csdms/ivy/commit/f90c87c04559ef90cec1eceead46ec975af39867) by Benjamin Campforts).
- Add toc item for text editors lesson ([60027c1](https://github.com/csdms/ivy/commit/60027c1e1cd90fe34fddcff0ae703d577247ee58) by Mark Piper).
- Add section on GitHub authentication (#68) ([dd4a3da](https://github.com/csdms/ivy/commit/dd4a3daa59dffd9316a954c94d8964d4f6bdb2e4) by Mark Piper).
- Add CSDMS logo and set as header logo ([7a706d1](https://github.com/csdms/ivy/commit/7a706d17f24745acf2fbe21ec19c7073087fc5aa) by Mark Piper).
- Add a helpful shell script ([5f78884](https://github.com/csdms/ivy/commit/5f788847a029f7e3c21d9935e0581fc1e0703dc8) by Mark Piper).

### Fixed

- Fix README notebook metadata (#67) ([4345f5f](https://github.com/csdms/ivy/commit/4345f5f7b5603310636372d8f1a3a36f4c7006cd) by Mark Piper).

### Changed

- Change landlab landing page ([5b97fd3](https://github.com/csdms/ivy/commit/5b97fd377a5b88418b13d44f1b26b1bdaa375695) by Benjamin Campforts).

### Removed

- Remove OS files not under version control ([e944a32](https://github.com/csdms/ivy/commit/e944a327c006b0857aa0515328b965143ff2fe0d) by Mark Piper).
- Remove solutions 5 and 6 ([d300794](https://github.com/csdms/ivy/commit/d30079423fa04fc3caa6c6d751b875901742be2d) by Benjamin Campforts).
- Remove stray apostrophe ([a984ba5](https://github.com/csdms/ivy/commit/a984ba5fc2af1828ec94cbc25fcd24cd2e1e6a04) by Mark Piper).

## [v1.1.1](https://github.com/csdms/ivy/releases/tag/v1.1.1) - 2022-03-09

<small>[Compare with v1.1](https://github.com/csdms/ivy/compare/v1.1...v1.1.1)</small>

### Added

- Add BMI overview slides to lesson ([d092cee](https://github.com/csdms/ivy/commit/d092ceeb877ad0f978268a47d82cdf5d789020ba) by Mark Piper).

## [v1.1](https://github.com/csdms/ivy/releases/tag/v1.1) - 2021-08-09

<small>[Compare with v1.0](https://github.com/csdms/ivy/compare/v1.0...v1.1)</small>

### Added

- add solution notebooks ([98f075e](https://github.com/csdms/ivy/commit/98f075ed7afaa16167bfc0c1d59ad83f7bc1c81d) by BCampforts).
- add solution notebook function ([dc8bb39](https://github.com/csdms/ivy/commit/dc8bb398f652f4a3a055a905b3d68acfd616da87) by BCampforts).
- add solutions ([534a805](https://github.com/csdms/ivy/commit/534a80550d552194fe4ae9165464d6faca38236a) by BCampforts).
- add new media files ([c9c6da1](https://github.com/csdms/ivy/commit/c9c6da1e43ad70241518988525546e721c503929) by BCampforts).
- add intro notes ([005a131](https://github.com/csdms/ivy/commit/005a13164e5fd388a81b672981fc3e1d67312939) by BCampforts).
- Add git remotes diagram for git lesson ([2ce7e7f](https://github.com/csdms/ivy/commit/2ce7e7f679b8697da0f6880460d96999ac327f50) by Mark Piper).
- Add link to 2021 schedule ([bd68ec8](https://github.com/csdms/ivy/commit/bd68ec8aee48da9135a3d92da3d1dbfe617ca585) by Mark Piper).
- Add DOI to citaton document ([e9d28b2](https://github.com/csdms/ivy/commit/e9d28b2aad028cd8e5757e96976113554966b036) by Mark Piper).

### Fixed

- Fix typo ([2966f43](https://github.com/csdms/ivy/commit/2966f43736ceaee4b5b796477a80a6c5f9d5109e) by Mark Piper).

### Removed

- remove solutions ([00e6ef0](https://github.com/csdms/ivy/commit/00e6ef06d27c6228372e1bb2f30f05c14212fdcd) by BCampforts).
- Remove executable bit ([307f782](https://github.com/csdms/ivy/commit/307f782a633648c92ae074c31db2c8add5811f15) by Mark Piper).

## [v1.0](https://github.com/csdms/ivy/releases/tag/v1.0) - 2020-08-24

<small>[Compare with v0.9](https://github.com/csdms/ivy/compare/v0.9...v1.0)</small>

### Added

- Add Resources section for shell lesson ([ec7a57e](https://github.com/csdms/ivy/commit/ec7a57e81743551f602f8656370f8a6c28e6d561) by Mark Piper).
- Add ref for managing conda environments ([54ceb17](https://github.com/csdms/ivy/commit/54ceb178eed7b5a2093b6ce87499e29ecf154c01) by Mark Piper).
- Add Travis CI config file ([c35eb73](https://github.com/csdms/ivy/commit/c35eb73f6ea83da613d6444716f1e781d86c5bf8) by Mark Piper).
- Add Clune & Rood reference for unit testing section ([e55e3d2](https://github.com/csdms/ivy/commit/e55e3d20f7af3f1c1f91a4444d0b93a04b022252) by Mark Piper).
- Add requirements for unit testing example ([e19174e](https://github.com/csdms/ivy/commit/e19174ed085b706ce36d053c5ea540c9cc3c127c) by Mark Piper).
- Add placeholder idnex file ([9105e26](https://github.com/csdms/ivy/commit/9105e26c1697a5b9e40179294d87bded00421292) by Mark Piper).
- Add sample Ku config file ([0e74e8c](https://github.com/csdms/ivy/commit/0e74e8c6e819c0e2e7c6d57ab7434d085ff53eaf) by Mark Piper).
- add landlab notebook ([3018610](https://github.com/csdms/ivy/commit/301861070033a701c19e84449da7a470c305f153) by BCampforts).
- Add BMI intro slides ([64fabff](https://github.com/csdms/ivy/commit/64fabffdbd53f97e21ac4f8b841738a64b92a3f9) by Mark Piper).
- add tidal flow calculator ([177a000](https://github.com/csdms/ivy/commit/177a0009cc2fac41be6a42b226b640440c4bad66) by iovereem).
- Add permafrost notebook to pymt lessons ([cdb8058](https://github.com/csdms/ivy/commit/cdb8058567e799f249378ac683b2e2d3a1f097a1) by iovereem).
- added header to OO lecture ([7811dd3](https://github.com/csdms/ivy/commit/7811dd312e3673edb55249f1b0fd0fc520042eab) by BCampforts).
- added OO lecture ([332c568](https://github.com/csdms/ivy/commit/332c5685a2607d1a3beb0e4ae96b44221abff28c) by BCampforts).

### Fixed

- Fix path to boulder_dem.py file ([7799ff4](https://github.com/csdms/ivy/commit/7799ff441ee43a6245e34eaa3e340ccbd9571c76) by Mark Piper).

### Changed

- Change name of gitiquette section ([5a13c45](https://github.com/csdms/ivy/commit/5a13c45eab6c143d5f8c6201e2305e70061549d0) by Mark Piper).
- Change lession directory from se to best-practices ([5bf7d9a](https://github.com/csdms/ivy/commit/5bf7d9ac36bbf972fb62ca8ff631a75e5d84e82d) by Mark Piper).

### Removed

- Remove index Notebook in favor of md file ([7512c08](https://github.com/csdms/ivy/commit/7512c08628358db45e39d8446cb697c923a1bed2) by Mark Piper).

## [v0.9](https://github.com/csdms/ivy/releases/tag/v0.9) - 2020-08-12

<small>[Compare with first commit](https://github.com/csdms/ivy/compare/fcfe84bbdf478ffbe9647f726005c678b1a67e78...v0.9)</small>

### Added

- Add data files ([0fac50d](https://github.com/csdms/ivy/commit/0fac50dbf518978476ea397e4ec871e9a20d250a) by BCampforts).
- Add short lesson on the conda package manager ([750e2a6](https://github.com/csdms/ivy/commit/750e2a60e482e7bf819d25ebfe750665218c7cb8) by Mark Piper).
- Add nbgitpuller link for Notebook tutorial ([e788d13](https://github.com/csdms/ivy/commit/e788d133be0d13f375dce79f5e5296003f224481) by Mark Piper).
- Add Notebook tutorial from Irina ([2ee37ed](https://github.com/csdms/ivy/commit/2ee37ed94d85692e1ec01fbd5470038cf2201e4a) by Mark Piper).
- Add instructions for collaboration ([988f2e8](https://github.com/csdms/ivy/commit/988f2e83babbd120486d846bab8d9da0eae9457f) by Mark Piper).
- Add permamodel toolkit to topics ([25e0d20](https://github.com/csdms/ivy/commit/25e0d201be854101ba35ec1436f81f0207477eb5) by Mark Piper).
- Add topics, links, instructors ([ce2a8ba](https://github.com/csdms/ivy/commit/ce2a8ba6cb54c03e75a391464eb88e864c6eca76) by Mark Piper).
- Add lesson on using git and GitHub collaboratively ([c98f0a5](https://github.com/csdms/ivy/commit/c98f0a55f985e0fce999001cc168e2bb9448e811) by Mark Piper).
- Added git cheat sheet ([dcf37c8](https://github.com/csdms/ivy/commit/dcf37c8d26e37e4b8a81cbca62419d067af2eedb) by iovereem).
- Add section on downloading ESPIn files as a zip archive ([60f48f9](https://github.com/csdms/ivy/commit/60f48f946ae3080dc26b120db25f85429adf3bf8) by Mark Piper).
- Add configuration section ([96a2d18](https://github.com/csdms/ivy/commit/96a2d18c7b94109cfef416bb3faf1c52c7df661f) by Mark Piper).
- Add Python example to be used for git lesson ([a747a44](https://github.com/csdms/ivy/commit/a747a44036ecfeb61c19af421e514433491913ad) by Mark Piper).
- Add content to getting things section ([575b2a2](https://github.com/csdms/ivy/commit/575b2a21b39a0ec5d14d7d3ca7f7819235c48500) by Mark Piper).
- Add content for finding things section ([c7e44ed](https://github.com/csdms/ivy/commit/c7e44ed200e2bbf9fe120c22388a2b0d715ca9a8) by Mark Piper).
- Add content for pipes and filters section ([e3de42a](https://github.com/csdms/ivy/commit/e3de42a315303c671b5eade90640bbb44c809ca8) by Mark Piper).
- Add hrule above nav links ([3b624fd](https://github.com/csdms/ivy/commit/3b624fd5d2fab626422a99a73cf2aa8f654f895f) by Mark Piper).
- Add content to Creating things section ([710059d](https://github.com/csdms/ivy/commit/710059da8bad213fb5d90a2dabeed88f5f168ffb) by Mark Piper).
- Add navigation to the end of each file ([bbc3833](https://github.com/csdms/ivy/commit/bbc38338e4a6ce92346bc7aaaf7d5b6ec9f2126a) by Mark Piper).
- Add summary table for commands in each section ([2ebc7d8](https://github.com/csdms/ivy/commit/2ebc7d8a16ce01df1cf4dd6382b15e1e4118ea83) by Mark Piper).
- Add README for viewing on GitHub ([cf6a719](https://github.com/csdms/ivy/commit/cf6a719aa0d4ce89cbff36ba1428f206958a21fc) by Mark Piper).
- Add content to lesson start ([61b8455](https://github.com/csdms/ivy/commit/61b8455f7b830893bf2158c387319126fd36a87b) by Mark Piper).
- Add ESPIn logo ([c7ada26](https://github.com/csdms/ivy/commit/c7ada26ead715b19fdd1fdb794954eb4853c2a2d) by Mark Piper).
- Add ESPIn logo to index Notebooks ([aead770](https://github.com/csdms/ivy/commit/aead77019d7573ae916beef8af3f4cb63a45ba94) by Mark Piper).
- Add ESPIn header image ([a4406ec](https://github.com/csdms/ivy/commit/a4406ec46f7bac9df772dfafb4f0b98b24a4f8ee) by Mark Piper).
- Add placeholder index Notebooks ([bb49493](https://github.com/csdms/ivy/commit/bb49493bb9f3be06a05bec71cb155a8aff008530) by Mark Piper).
- Add pymt lesson material ([d76e61c](https://github.com/csdms/ivy/commit/d76e61c0e82b0cbe08cf9e9add6f7583ddc7fef9) by Mark Piper).
- Add conda environment file for lessons ([3aecf94](https://github.com/csdms/ivy/commit/3aecf94f1a6d3b73ede776c08babaa8dc6e3b7ee) by Mark Piper).
- Add Landlab Notebooks and data ([4951ac7](https://github.com/csdms/ivy/commit/4951ac7899b58c88fe943a79659a680a274933c0) by Mark Piper).
- Add first pass at BMI lessons ([34a0136](https://github.com/csdms/ivy/commit/34a0136a75ef6b276e09a9e908945038cef0f664) by Mark Piper).
- Add CSDMS product images for use in Notebooks ([66813eb](https://github.com/csdms/ivy/commit/66813eb0f1139bccfb9f4ff6be096bc385db72f6) by Mark Piper).

### Fixed

- Fix remaining links ([ad8bd62](https://github.com/csdms/ivy/commit/ad8bd620f10ca6c9fca23a5ad094c2ab7c25e871) by Mark Piper).
- Fix broken link to logo ([78acace](https://github.com/csdms/ivy/commit/78acace58bb7ed8cbf502d8f40364f0278c9627f) by Mark Piper).

### Changed

- change index to link ([7ecdeb8](https://github.com/csdms/ivy/commit/7ecdeb8e4f6d28ba98dc2ad3f36f3fe17e8c0b3e) by BCampforts).
- changes in headers and layout ([29d1713](https://github.com/csdms/ivy/commit/29d1713e18d718b8c1fadf4e8036488d979ad9e9) by BCampforts).
- Change index.ipynb to a link ([6bfa67c](https://github.com/csdms/ivy/commit/6bfa67c53e94c5051167db8eb3c20bb16db922f7) by Mark Piper).
- Change topic heading titles ([52049b3](https://github.com/csdms/ivy/commit/52049b35b9a6aea0d4beac2ae0f83528cbda96d2) by Mark Piper).

### Removed

- Remove index Notebook in favor of md file ([06bd408](https://github.com/csdms/ivy/commit/06bd4080df722e7d16f6b77cb2dbe92964fd0a31) by Mark Piper).
