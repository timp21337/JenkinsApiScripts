__author__ = 'timp'

g_projects = []
g_repos = {}
g_branches = {}
g_operations = {}
g_owners = {}


class Project():
  """A jenkins project"""

  def __init__(self, original, repo, branch, operation, owner):
    self.original = original
    self.repo = repo
    self.branch = branch
    self.operation = operation
    self.owner = owner

    if g_repos.get(repo) != None:
      g_repos[repo] = g_repos[repo] + 1
    else:
      g_repos[repo] = 1

    if g_branches.get(branch) != None:
      g_branches[branch] = g_branches[branch] + 1
    else:
      g_branches[branch] = 1

    if g_operations.get(operation) != None:
      g_operations[operation] = g_operations[operation] + 1
    else:
      g_operations[operation] = 1

    if g_owners.get(owner) != None:
      g_owners[owner] = g_owners[owner] + 1
    else:
      g_owners[owner] = 1


  def name(self):
#    return "{}.{}.{}.{}".format(self.owner, self.repo, self.branch, self.operation)
    return "{}.{}.{}.{}".format(self.repo, self.branch, self.operation, self.owner)

  def __str__(self):
    return "{:<58} => {}".format(self.original, self.name())
#    return "{:<58} => {}.{}.{}.{}".format(self.original, self.repo, self.branch, self.operation, self.owner)


  def __repr__(self):
    return self.__str__()

  def __lt__(self, other):
    if self.repo == other.repo:
      if self.branch == other.branch:
        if self.operation == other.operation:
          return self.owner < other.owner
        else:
          return self.operation < other.operation
      else:
        return self.branch < other.branch
    else:
      return self.repo < other.repo


def l(original, repo, branch, operation, owner):
  project = Project(original, repo, branch, operation, owner)
  g_projects.append(project)




l('api-vagrant', 'api', 'develop', 'vagrant', 'core')
l('build-api', 'api', 'develop', 'build-ant', 'core')
l('BackupToGit', 'jenkins', 'hades', 'backup', 'det')
l('build-admin', 'admin', 'develop', 'build-ant', 'web')
l('build-api-gradle', 'api', 'develop', 'build-gradle', 'core')
l('build-api-keith-test', 'api', 'test', 'build-ant', 'keith')
l('build-api-master', 'api', 'master', 'build-ant', 'core')
l('build-api-pull-requests', 'api', '_pr_', 'build-ant', 'core')
l('build-api-release-ordog', 'api', 'release_ordog', 'build-ant', 'core')
l('build-api-release-paimon', 'api', 'release_paimon', 'build-ant', 'core')
l('build-api-release-ravana', 'api', 'release_ravana', 'build-ant', 'core')
l('build-api-release-succubus', 'api', 'release_succubus', 'build-ant', 'core')
l('build-api-vagrant', 'api', 'develop', 'build-ant-vagrant', 'core')
l('build-bunk', 'bunk.js', 'develop', 'build-ant', 'web')
l('build-data-mining', 'data-mining', 'develop', 'build-ant', 'radio')
l('build-data-mining-master', 'data-mining', 'master', 'build-ant', 'radio')
l('build-data-mining-release', 'data-mining', 'release', 'build-ant', 'radio')
l('build-email-utils-release-eku', 'email-utils', 'release_eku', 'build-ant', 'core')
l('build-email-utils-release-flintlock', 'email-utils', 'release_flintlock', 'build-ant', 'core')
l('build-events-warehouse-distributed', 'events-warehouse', 'develop', 'build-ant', 'warehouse')
l('build-events-warehouse-distributed-latest-release', 'events-warehouse', 'release', 'build-ant', 'warehouse')
l('build-events-warehouse-distributed-part1', 'events-warehouse', 'develop', 'part1', 'warehouse')
l('build-events-warehouse-distributed-part1-latest-release', 'events-warehouse', 'release', 'part1', 'warehouse')
l('build-events-warehouse-distributed-part2', 'events-warehouse', 'develop', 'part2', 'warehouse')
l('build-events-warehouse-distributed-part2-latest-release', 'events-warehouse', 'release', 'part2', 'warehouse')
l('build-image-server', 'image-server', 'develop', 'build-ant', 'core')
l('build-image-server-release-andy-warhol', 'image-server', 'release_andy-warhol', 'build-ant', 'core')
l('build-lyricfind', 'lyricfind', 'develop', 'build-ant', 'core')
l('build-lyricfind-release-chattanooga', 'lyricfind', 'release_chattanooga', 'build-ant', 'core')
l('build-massupload-client', 'mass-upload-client', 'develop', 'build-gradle', 'core')
l('build-massupload-client-atreus', 'mass-upload-client', 'develop_atreus', 'build-gradle', 'core')
l('build-origami', 'origami', 'develop', 'build-gradle', 'core')
l('build-paperplane', 'paperplane', 'develop', 'build-ant', 'warehouse')
l('build-popularity', 'popularity', 'develop', 'build-ant', 'radio')
l('build-python-core', 'python-core', 'develop', 'build-ant', 'core')
l('build-radio-site', 'radio-site', 'develop', 'build-ant', 'web')
l('build-radio-site-pull-requests', 'radio-site', '_pr_', 'build-ant', 'web')
l('build-radio-site-release', 'radio-site', 'release_gambit-1', 'build-ant', 'web')
l('build-recommendations', 'recommendations', 'develop', 'build-ant', 'radio')
l('build-tempo-tracker', 'tempo-tracker', 'develop', 'build-ant', 'radio')
l('build-trackversions', 'track-versions', 'develop', 'build-ant', 'core')
l('build-tvapp', 'browserapp', 'develop', 'deployOnBuildMachine', 'tvapp')
l('build-tvapp-qa', 'browserapp', 'develop', 'deployQAOnBuildMachine', 'tvapp')
l('build-WAIF', 'WAIF', 'develop', 'build-ant', 'web')
l('build-warehouse-reporting', 'warehouse-reporting', 'develop', 'build-ant', 'warehouse')
l('build-warehouse-reporting-latest-release', 'warehouse-reporting', 'release', 'build-ant', 'warehouse')
l('build-we7-pig-unit', 'events-warehouse', 'develop', 'pig-unit-tests', 'warehouse')
l('build-we7-pig-unit-ducktails', 'events-warehouse', 'release_23_ducktales', 'pig-unit-tests', 'warehouse')
l('build-we7-pig-unit-latest-release', 'events-warehouse', 'release', 'pig-unit-tests', 'warehouse')
l('build-we7-subprojects', 'events-warehouse', 'develop', 'unit-test-subprojects', 'warehouse')
l('build-we7-subprojects-latest-release', 'events-warehouse', 'release', 'unit-test-subprojects', 'warehouse')
l('build-wez-js', 'wez.js', 'develop', 'build-ant', 'web')
l('build-zeppelin', 'zeppelin', 'develop', 'build-ant', 'core')
l('build-zeppelin-release-avro', 'zeppelin', 'release_avro', 'build-ant', 'core')
l('checkstyle-events-warehouse', 'events-warehouse', 'develop', 'pylint', 'warehouse')
l('checkstyle-we7-hive-udfs', 'events-warehouse', 'develop', 'hive-udfs-checkstyle', 'warehouse')
l('checkstyle-we7-pig-udfs', 'events-warehouse', 'develop', 'pig-udfs-checkstyle', 'warehouse')
l('checkstyle-we7-pig-unit', 'events-warehouse', 'develop', 'pig-unit-checkstyle', 'warehouse')
l('config-code-style', 'code-style', 'master', 'deploy', 'det')
l('cucumber-api', 'api', 'develop', 'cucumber-ant', 'core')
l('cucumber-api-gradle', 'api', 'develop', 'cucumber-gradle', 'core')
l('cucumber-api-tim', 'api', 'develop', 'cucumber-ant', 'timp')
l('cucumber-api-vagrant', 'api', 'develop', 'cucumber-ant-vagrant', 'core')
l('DET-BUILD-APIA', 'api', 'develop', 'provide-server-det-apia', 'det')
l('DET_Android_LargeTest', 'we7-Android', 'develop', 'cucumber', 'det')
l('DET_iOS_LargeTest', 'we7-iOS', 'develop', 'cucumber', 'det')
l('DET_RadioSite_API_DEVELOP', 'testdb-creator', 'develop', 'provide_server_dev', 'det')
l('DET_RadioSite_API_DEVELOP2', 'testdb-creator', 'develop', 'provide_server_dev-fast', 'det')


# release here refers to the version in vagrant
l('DET_RadioSite_API_RELEASE', 'testdb-creator', 'release', 'provide_server_rel', 'det')
l('DET_RadioSite_DEVELOP', 'radio-site', 'develop', 'delete-me-someday', 'det')
l('DET_RADIOSITE_DEVELOP_FAST', 'radio-site', 'develop', 'meta-cucumber-fast', 'det')
l('DET_RADIOSITE_DEVELOP_IE', 'radio-site', 'develop', 'meta-cucumber-ie', 'det')

l('DET_RADIOSITE_DEVELOP_SLOW', 'radio-site', 'develop', 'meta-cucumber-all', 'det')
l('DET_RadioSite_DEVELOP_streamLog', 'radio-site', 'develop', 'meta-cucumber-large', 'det')
l('DET_RADIOSITE_LargeTest', 'radio-site', 'develop', 'cucumber-large', 'det')
l('DET_RadioSite_PREREL', 'radio-site', 'prerel', 'delete-me-someday', 'det')
l('DET_RadioSite_RELEASE', 'radio-site', 'release', 'delete-me-someday', 'det')
l('DET_RADIOSITE_RELEASE_FAST', 'radio-site', 'release', 'meta-cucumber-fast', 'det')
l('DET_RADIOSITE_RELEASE_SLOW', 'radio-site', 'release', 'meta-cucumber-all', 'det')
l('DET_StagingA_RadioSite', 'radio-site', 'develop', 'cucmber-staginga', 'det')
l('DET_StagingB_RadioSite', 'radio-site', 'develop', 'cucmber-stagingb', 'det')
l('DET_StagingC_RadioSite', 'radio-site', 'develop', 'cucmber-stagingc', 'det')
l('DET_StagingD_RadioSite', 'radio-site', 'develop', 'cucmber-stagingd', 'det')
l('DET_StagingE_RadioSite', 'radio-site', 'develop', 'cucmber-staginge', 'det')
l('DET_StagingF_RadioSite', 'radio-site', 'develop', 'cucmber-stagingf', 'det')
l('DET_Test_DB_Creator', 'testdb-creator', 'develop', 'createdb', 'det')
l('DET_Test_DB_Creator2', 'testdb-creator', 'develop', 'delete-me-someday', 'det')

l('DET_W7_CH_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-chrome', 'det')
l('DET_W7_CH_RELEASE', 'radio-site', 'release', 'cucumber-win7-chrome', 'det')
l('DET_W7_FF_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-firefox', 'det')
l('DET_W7_FF_RELEASE', 'radio-site', 'release', 'cucumber-win7-firefox', 'det')
l('DET_W7_IE10_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-ie10', 'det')
l('DET_W7_IE10_RELEASE', 'radio-site', 'release', 'cucumber-win7-ie10', 'det')
l('DET_W7_IE11_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-ie11', 'det')
l('DET_W7_IE8_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-ie8', 'det')
l('DET_W7_IE8_RELEASE', 'radio-site', 'release', 'cucumber-win7-ie8', 'det')
l('DET_W7_IE9_DEVELOP', 'radio-site', 'develop', 'cucumber-win7-ie9', 'det')
l('DET_W7_IE9_RELEASE', 'radio-site', 'release', 'cucumber-win7-ie9', 'det')
l('DET_W8_IE10_DEVELOP', 'radio-site', 'develop', 'cucumber-win8-ie10', 'det')
l('DET_W8_IE10_RELEASE', 'radio-site', 'release', 'cucumber-win8-ie10', 'det')
l('DET_Wheezy_Chrome_DEVELOP', 'radio-site', 'develop', 'cucumber-wheezy-chrome', 'det')
l('DET_Wheezy_Chrome_RELEASE', 'radio-site', 'release', 'cucumber-wheezy-chrome', 'det')
l('DET_Wheezy_Firefox_DEVELOP', 'radio-site', 'develop', 'cucumber-wheezy-firefox', 'det')
l('DET_Wheezy_Firefox_RELEASE', 'radio-site', 'release', 'cucumber-wheezy-firefox', 'det')
l('DET_Wheezy_UnsupportedBrowser_DEVELOP', 'radio-site', 'develop', 'cucumber-Wheezy-UnsupportedBrowser', 'det')
l('DET_Wheezy_UnsupportedBrowser_RELEASE', 'radio-site', 'release', 'cucumber-Wheezy_UnsupportedBrowser', 'det')
l('DET_XP_IE8_DEVELOP', 'radio-site', 'develop', 'cucumber-winxp-ie8', 'det')
l('DET_XP_IE8_RELEASE', 'radio-site', 'release', 'cucumber-winxp-ie8', 'det')

l('essential-test-events-warehouse-distributed', 'events-warehouse', 'develop', 'xmlEssentialTests', 'warehouse')
l('essential-test-events-warehouse-distributed-ducktales', 'events-warehouse', 'release_23_ducktales',
  'xmlEssentialTests', 'warehouse')
l('essential-test-events-warehouse-distributed-latest-release', 'events-warehouse', 'release', 'xmlEssentialTests',
  'warehouse')
l('essential-test-events-warehouse-distributed-pull-requests', 'events-warehouse', '_pr_', 'xmlEssentialTests',
  'warehouse')
l('events-api-build', 'events-api', 'develop', 'build-build', 'warehouse')
l('events-api-release-actinium', 'events-api', 'release_actinium', 'build-gradle', 'warehouse')
l('events-api-sonar', 'events-api', 'develop', 'sonar', 'warehouse')
l('events-domain', 'events-domain', 'develop', 'deploy', 'warehouse')
l('events-idl', 'events-idl', 'develop', 'pushChangesToEventIdIosRepo-gradle', 'warehouse')

# parameterised, defaulted to release/*
l('events-idl', 'events-idl', 'release', 'pushChangesToEventIdIosRepo-gradle', 'warehouse')

# # also hotfix
l('events-storm', 'events-storm', 'develop', 'install-mvn', 'warehouse')

l('events-storm-mutate', 'events-storm', 'develop', 'pitest-mvn', 'warehouse')

l('events-warehouse-vagrant-end-to-end-test', 'events-warehouse', 'develop', 'vagrant-end-to-end-test', 'warehouse')
l('events-warehouse-vagrant-end-to-end-test-ducktales', 'events-warehouse', '23_ducktales', 'vagrant-end-to-end-test',
  'warehouse')
l('events-warehouse-vagrant-end-to-end-test-events-vagrant', 'events-warehouse', 'feauture_add-pig-processing-to-end-to-end-tests', 'vagrant-end-to-end-test',
  'warehouse')
l('events-warehouse-vagrant-end-to-end-test-experimental', 'events-warehouse', 'feature_curb_yarn',
  'vagrant-end-to-end-test', 'warehouse')
l('events-warehouse-vagrant-end-to-end-test-latest-release', 'events-warehouse', 'release', 'vagrant-end-to-end-test',
  'warehouse')
l('events-warehouse-vagrant-end-to-end-test-localmode', 'events-warehouse', 'yrro_local-mode',
  'vagrant-end-to-end-test', 'warehouse')
l('events-warehouse-vagrant-end-to-end-test-parallel', 'events-warehouse', 'feature_parallel-hive-jobs',
  'vagrant-end-to-end-test', 'warehouse')

l('events-warehouse-vagrant-integration-localmode', 'events-warehouse', 'yrro_local-mode', 'vagrant-integration-test',
  'warehouse')

l('findbugs-api', 'api', 'develop', 'findbugs-ant', 'core')
l('findbugs-radio-site', 'radio-site', 'develop', 'findbugs-ant', 'core')

# Not in a repo
l('generate-api-docs', 'api', 'develop', 'generate-rest-api-docs', 'core')

l('gracenote-fingerprinter-build', 'gracenote-fingerprinter', 'develop', 'build-gradle', 'research')
l('gracenote-matcher-build', 'gracenote-matcher', 'develop', 'build-gradle', 'research')
l('iOS-develop-intraday-frank-tests', 'we7-iOS', 'develop', 'intraday-frank-tests', 'ios')
l('iOS-develop-nightly-all', 'we7-iOS', 'develop', 'ci-all', 'ios')
l('iOS-develop-nightly-frank-tests', 'we7-iOS', 'develop', 'nightly-frank-tests', 'ios')
l('iOS-develop-unit-tests', 'we7-iOS', 'develop', 'unit-test-bash', 'ios')
l('iOS-hotfix-intraday-frank-tests', 'we7-iOS', 'hotfix', 'intraday-frank-tests', 'ios')
l('iOS-hotfix-unit-tests', 'we7-iOS', 'hotfix', 'unit-test-bash', 'ios')
l('iOS-pull-requests', 'we7-iOS', '_pr_', 'unit-test-bash', 'ios')
l('iOS-release-frank-tests', 'we7-iOS', 'release', 'frank-tests', 'ios')

#just release ?
l('iOS-release-unit-tests', 'we7-iOS', 'release-3.5', 'unit-test-bash', 'ios')

#l('Jenkins-draw-views', 'jenkins-graphviz', 'master', 'draw-jenkins-views', 'det')

l('metadata-api', 'metadata-ap', 'develop', 'build-api-gradle', 'research')
l('metadata-api-integration-test', 'metadata-ap', 'develop', 'test-vagrant', 'research')
l('metadata-client', 'metadata-ap', 'develop', 'build-client-gradle', 'research')

l('mutate-api', 'api', 'develop', 'pitest-gradle', 'core')
l('mutate-radio-site', 'radio-site', 'develop', 'pitest-ant', 'web')
l('package-bbm-admin', 'admin', 'master', 'deb_build_pkg', 'no')
l('package-bbm-api', 'api', 'master', 'deb_build_pkg', 'no')
l('package-bbm-ops-services', 'ops-services', 'master', 'deb_build_pkg', 'no')
l('package-content-encoder-develop', 'content-encoder', 'develop', 'deb_build_script', 'no')
l('package-content-encoder-release', 'content-encoder', 'tags_release', 'deb_build_script', 'no')
l('package-content-encoder-staging', 'content-encoder', 'release', 'deb_build_script', 'no')
l('package-data-mining-develop', 'data-mining', 'develop', 'deb_build_script', 'no')
l('package-data-mining-release', 'data-mining', 'tags_release', 'deb_build_script', 'no')
l('package-data-mining-staging', 'data-mining', 'release', 'deb_build_script', 'no')
l('package-dh-bbm-info', 'dh-bbm-info', 'master', 'deb_build_script', 'no')
l('package-dh-bbm-info-develop', 'dh-bbm-info', 'develop', 'deb_build_script', 'no')
l('package-dh-bbm-info-release', 'dh-bbm-info', 'tags_release', 'deb_build_script', 'no')
l('package-dh-bbm-info-staging', 'dh-bbm-info', 'release', 'deb_build_script', 'no')
l('package-dh-virtualenv-develop', 'dh-virtualenv', 'develop', 'deb_build_script', 'no')
l('package-dh-virtualenv-release', 'dh-virtualenv', 'tags_release', 'deb_build_script', 'no')
l('package-dh-virtualenv-staging', 'dh-virtualenv', 'release', 'deb_build_script', 'no')
l('package-email-utils-develop', 'email-utils', 'develop', 'deb_build_script', 'no')
l('package-email-utils-release', 'email-utils', 'tags_release', 'deb_build_script', 'no')
l('package-email-utils-staging', 'email-utils', 'release', 'deb_build_script', 'no')
l('package-events-api-develop', 'events-api', 'develop', 'deb_build_script', 'no')
l('package-events-api-release', 'events-api', 'tags_release', 'deb_build_script', 'no')
l('package-events-api-staging', 'events-api', 'release', 'deb_build_script', 'no')
l('package-events-warehouse-develop', 'events-warehouse', 'develop', 'deb_build_script', 'no')
l('package-events-warehouse-release', 'events-warehouse', 'tags_release', 'deb_build_script', 'no')
l('package-events-warehouse-staging', 'events-warehouse', 'release', 'deb_build_script', 'no')
l('package-gracenote-fingerprinter', 'gracenote-fingerprinter', 'develop', 'deb_build_pkg', 'no')
l('package-image-server-develop', 'image-server', 'develop', 'deb_build_script', 'no')
l('package-image-server-release', 'image-server', 'tags_release', 'deb_build_script', 'no')
l('package-image-server-staging', 'image-server', 'release', 'deb_build_script', 'no')

# also watching release
l('package-imageserver', 'image-server', 'master', 'deb_build_pkg', 'no')

l('package-init-system-helpers', 'init-system-helpers', '_param_', 'deb_build_script', 'no')
l('package-limnoria', 'Limnoria', 'tags_release', 'deb_build_script', 'no')
l('package-logprocessing-release', 'logprocessing', 'tags_release', 'deb_build_script', 'no')
l('package-lyricfind-develop', 'lyricfind', 'develop', 'deb_build_script', 'no')
l('package-lyricfind-release', 'lyricfind', 'tags_release', 'deb_build_script', 'no')
l('package-lyricfind-staging', 'lyricfind', 'release', 'deb_build_script', 'no')
l('package-mediagraft-develop', 'api', 'develop', 'deb_build_script', 'no')
l('package-munin-plugins-we7-release', 'munin-plugins-we7', 'tags_release', 'deb_build_script', 'no')
l('package-opsview-agent-we7-release', 'opsview-agent-we7', 'release', 'deb_build_script', 'no')
l('package-origami-develop', 'origami', 'develop', 'deb_build_script', 'no')
l('package-origami-release', 'origami', 'tags_release', 'deb_build_script', 'no')
l('package-origami-staging', 'origami', 'release', 'deb_build_script', 'no')
l('package-popularity-develop', 'popularity', 'develop', 'deb_build_script', 'no')
l('package-popularity-release', 'popularity', 'tags_release', 'deb_build_script', 'no')
l('package-popularity-staging', 'popularity', 'release', 'deb_build_script', 'no')
l('package-python-core-develop', 'python-core', 'develop', 'deb_build_script', 'no')
l('package-python-core-release', 'python-core', 'tags_release', 'deb_build_script', 'no')
l('package-python-core-staging', 'python-core', 'release', 'deb_build_script', 'no')

#wat master and release
l('package-recommendations', 'recommendations', '_any_', 'deb_build_pkg', 'no')

l('package-stormproject', 'stormproject', '_param_', 'deb_build_script', 'no')
l('package-tcollector', 'tcollector', '_any_', 'deb_build_pkg', 'no')
l('package-tempo-tracker-develop', 'tempo-tracker', 'develop', 'deb_build_script', 'no')
l('package-tempo-tracker-release', 'tempo-tracker', 'tags_release', 'deb_build_script', 'no')
l('package-tempo-tracker-staging', 'tempo-tracker', 'release', 'deb_build_script', 'no')
l('package-warehouse-reporting-develop', 'warehouse-reporting', 'develop', 'deb_build_script', 'no')
l('package-warehouse-reporting-release', 'warehouse-reporting', 'tags_release', 'deb_build_script', 'no')
l('package-warehouse-reporting-staging', 'warehouse-reporting', 'release', 'deb_build_script', 'no')
l('package-zeppelin-develop', 'zeppelin', 'develop', 'deb_build_script', 'no')
l('package-zeppelin-release', 'zeppelin', 'tags_release', 'deb_build_script', 'no')
l('package-zeppelin-staging', 'zeppelin', 'release', 'deb_build_script', 'no')
l('pickle-test', 'we7-iOS', 'develop', 'pickle-test', 'ios')

l('puppet-null', 'puppet', 'master', 'trigger-vagrant-builds', 'det')
l('puppet-rspec', 'puppet', 'master', 'rspec', 'no')
l('puppet-smoketest', 'puppet', 'master', 'smoketest', 'no')
l('rest-doclet', 'rest-doclet', 'develop', 'install-mvn', 'edward')
l('rest-doclet-travis', 'rest-doclet', 'develop', 'groovy-parse', 'edward')
l('schemaspy-testpodsplice', 'api', 'develop', 'schemaspy', 'det')
l('search-build', 'search', 'develop', 'build-gradle', 'core')
l('SMTPListener', 'SMTPListener', 'develop', 'install-mvn', 'det')
l('sonar-api', 'api', 'develop', 'sonar', 'det')
l('sonar-lyricfind', 'lyricfind', 'develop', 'sonar', 'det')
l('sonar-origami', 'origami', 'develop', 'sonar', 'det')
l('sonar-popularity', 'popularity', 'develop', 'sonar', 'det')
l('sonar-python-core', 'python-core', 'develop', 'sonar', 'det')
l('sonar-radio-site', 'radio-site', 'develop', 'sonar', 'det')
l('sonar-recommendations', 'recommendations', 'develop', 'sonar', 'det')

l('tomcat-helper-build', 'tomcat-session', 'develop', 'build-gradle', 'core')
l('tomcat-session-build', 'utilities', 'develop', 'build-gradle', 'core')
l('test-events-pipeline', 'test-events-pipeline', 'develop', 'vagrant-build', 'warehouse')
l('unittest-events-warehouse', 'events-warehouse', 'develop', 'unit-test-ant', 'warehouse')
l('unittest-events-warehouse-latest-release', 'events-warehouse', 'release', 'unit-test-ant', 'warehouse')
l('unittest-events-warehouse-pull-requests', 'events-warehouse', '_pr_', 'unit-test-ant', 'warehouse')
l('we7-android-daniele', 'we7-Android', '_any_', 'test', 'daniele')
l('we7-android-develop', 'we7-Android', 'develop', 'test', 'android')
l('we7-android-develop-MarketKey', 'we7-Android', 'develop', 'marketKey', 'android')
l('we7-android-frontiersilicon', 'we7-Android', 'develop', 'frontiersilicon', 'android')
l('we7-android-hotfix', 'we7-Android', 'hotfix', 'test', 'android')
l('we7-android-hotfix-marketKey', 'we7-Android', 'hotfix', 'marketKey', 'android')
l('we7-android-hotfix-marketKey-notDebuggable', 'we7-Android', 'hotfix', 'marketKey-notDebuggable', 'android')
l('we7-android-master', 'we7-Android', 'master', 'test', 'android')
l('we7-android-master-debugKey', 'we7-Android', 'master', 'test-debugKey', 'android')
l('we7-android-pull-requests', 'we7-Android', '_pr_', 'test', 'android')
l('we7-android-release', 'we7-Android', 'release', 'test', 'android')
l('we7-android-release-marketKey-debuggableFalse', 'we7-Android', 'release', 'marketKey-debuggableFalse', 'android')
l('we7-android-release-marketSignature', 'we7-Android', 'release', 'marketSignature', 'android')
l('we7-android-special-release', 'we7-Android', 'release', 'special', 'android')
l('we7-calabash-android', 'we7-Android', 'develop', 'calabash', 'android')
l('we7-calabash-android-nightly-build', 'we7-Android', 'develop', 'calabash-nightly', 'android')

l('we7-shared-build', 'shared-jar', 'develop', 'build-gradle', 'core')

l('windows-develop', 'bbm-windows', 'develop', 'vs-build-test', 'windows')
l('windows-develop-mystation', 'bbm-windows', 'develop.MyStation', 'vs-build-test', 'windows')

#wat
l('windows-develop-release', 'bbm-windows', 'develop', 'vs-build-test-release', 'windows')
l('windows-pull-requests', 'bbm-windows', '_pr_', 'vs-build-test', 'windows')
l('windows-testbench', 'bbm-windows', 'develop', 'vs-testbench', 'windows')


def attributes(object_list, att_name):
  atts = {}
  for o in object_list:
    if atts.get(o.__dict__[att_name]) != None:
      atts[o.__dict__[att_name]] += 1
    else:
      atts[o.__dict__[att_name]] = 1
  return atts

def repos(project_list):
  return attributes(project_list, 'repo')

def branches(project_list):
  return attributes(project_list, 'branch')

def operations(project_list):
  return attributes(project_list, 'operation')

def owners(project_list):
  return attributes(project_list, 'owner')

def report_list(_list):
  print "\nJobs ({})".format(len(_list))
  print "{}".format('-' * 9)
  for p in sorted(_list):
    print(p)

def names(_list):
  print "\nJobs ({})".format(len(_list))
  print "{}".format('-' * 9)
  for p in sorted(_list):
    print(p.name())

def report_dic(name, dic):
  print "\n{} ({})".format(name, len(dic))
  print "{}".format('-' * (len(name) + 5))
  for e in sorted(dic):
    print("{} {}".format(e, dic[e]))


def report():
  report_list(g_projects)
  report_dic("Repos", g_repos)
  report_dic("Branches", g_branches)
  report_dic("Operations", g_operations)
  report_dic("Owners", g_owners)
  new_names = {}
  for p in g_projects:
    if new_names.get(p.name()) != None:
      new_names[p.name()] = new_names[p.name()] + 1
      print "****Duplicate name: {}".format(p.name())
    else:
      new_names[p.name()] = 1



def report_team(team):
  team_list = [i for i in g_projects if i.owner == team]
  report_dic("Owners", owners(team_list))
  report_list(team_list)
  report_dic("Repos", repos(team_list))
  report_dic("Branches", branches(team_list))
  report_dic("Operations", operations(team_list))


def print_renames(team):
  print('import jenkinsapi')
  print('from jenkinsapi.jenkins import Jenkins')
  print("J = Jenkins('http://hades:8081', 'timp', '94bff6285f22db83e8de27b27cf69263')")
  team_list = [i for i in g_projects if i.owner == team]
  for p in team_list:
    print("J.rename_job('{}', '{}')".format(p.original, p.name()))






#report_team('core')

#print_renames('core')
#print_renames('det')
#print_renames('edward')
#print_renames('keith')
#print_renames('no')
#print_renames('radio')
#print_renames('research')
#print_renames('timp')
#print_renames('web')


# Outstanding
#print_renames('android')
#print_renames('daniele')
#print_renames('ios')
#print_renames('tvapp')
#print_renames('warehouse')
#print_renames('windows')



#report_list(g_projects)
#names(g_projects)

report()